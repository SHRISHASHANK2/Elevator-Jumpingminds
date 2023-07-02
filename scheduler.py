import math

n_floors = 20 # number of floors

t_door = 1.5
t_psg = 1.5



class Scheduler:
    @staticmethod
    def selectElevators(waiting_list, elevators):
        # print('#0 y: ', elevators[0].y_inst)
        if len(waiting_list) > 0:
            for psg in waiting_list:
                choiceElv = elevators[0]
                for elv in elevators:
                    choiceFS = choiceElv.calculateFS(n_floors, yPassenger=psg.y1, landingCall=psg.y2)
                    elvFS = elv.calculateFS(n_floors, yPassenger=psg.y1, landingCall=psg.y2)
                    # print('choice fs:', choiceFS, 'elv fs:', elvFS)
                    if elvFS > choiceFS or (
                            elvFS == choiceFS and (abs(elv.y_inst - psg.y1) < abs(choiceElv.y_inst - psg.y1))):
                        choiceElv = elv
                    psg.choiceElv = choiceElv
                # print('chosen elevator:', psg.choiceElv._id)

                if psg.choiceElv.y_goal == None and psg.choiceElv.state != 'stop':
                    psg.choiceElv.y_goal = psg.y1

    @staticmethod
    def moveElevators(elevators, dt):
        for elv in elevators:
            if elv.state == 'moving':
                print('id:', elv._id, '|',  elv.y_begin, elv.y_goal, elv.filling)
                elv.travel(dt)



    # @staticmethod
    # def goForPickup(elevator, psg, v, a, j, t, dt):
    #     elevator.y_goal = psg.y1
    #     if elevator.y_begin == psg.y1:
    #         t_el_showup = 0
    #         elevator.state = 'stop'
    #         elevator.y_begin = psg.y1
    #     else:
    #         t_el_showup = elevator.travel(v, a, j, dt)
    #         if t < psg.arrTime + t_el_showup:
    #             elevator.state = 'moving'
    #         else:
    #             elevator.state = 'stop'
    #             elevator.y_begin = psg.y1
    #
    #     return  t_el_showup
    #
    #
    #
    #

    @staticmethod
    def dropoff_passengers(elevators, dt):
        for elv in elevators:
            elv_flr = math.floor(elv.y_inst)
            if len(elv.passengers) > 0 and elv.state == 'moving':
                drops = [psg for psg in elv.passengers if psg.y2 == elv_flr]
                # print(drops)
                n_drops = len(drops)
                if n_drops > 0:
                    elv.state = 'stop'
                    elv.y_inst = drops[0].y2
                    elv.t_door_psg = 2 * t_door + n_drops * t_psg
                    elv.filling = -1

            elif elv.state == 'stop' and elv.y_goal != None and elv.filling == -1:
                drops = [psg for psg in elv.passengers if psg.y2 == elv_flr]
                print(drops)
                n_drops = len(drops)
                elv.t_door_psg -= dt
                # if elv._id == 0:
                #     print('here:', elv.t_door_psg - 2 * t_door, 'remainder:', (elv.t_door_psg - t_door) % t_psg)
                #
                if round(elv.t_door_psg % t_psg, 2) == 0 and elv.t_door_psg > t_door and elv.t_door_psg < 2 * t_door + n_drops * t_psg - t_door:
                    # print('working correctly')
                    if len(drops) > 0:
                        dropItem = drops.pop(0)
                        elv.passengers.remove(dropItem)
                elif elv.t_door_psg == 0:
                    elv.filling = 0

                if len(elv.passengers) == 0 and elv.t_door_psg <= 0:
                    elv.y_begin = elv.y_goal
                    elv.y_goal = None
                    elv.t_door_psg = None
                    elv.filling = 0

            if elv.state == 'moving' and elv.t_door_psg != None:
                elv.t_door_psg = None
                # print('yes')












    @staticmethod
    def pickup_passengers(elevators, waiting_list, dt):
        for elv in elevators:
            # print('elevator:', elv.state, 'goal:', elv.y_goal)
            if elv.state == 'stop' and elv.y_goal == None and elv.filling == 1:
                # print('triggered')
                elv.passengers = [psg for psg in waiting_list if psg.choiceElv == elv]
                for psg in elv.passengers:
                    waiting_list.remove(psg)

                # print('elev passengers:', elv.passengers)
                if len(elv.passengers) > 0:
                    # print('this is setting that')
                    elv.y_goal = elv.passengers[0].y2
                    elv.t_door_psg = 2 * t_door + len(elv.passengers) * t_psg
                    elv.filling = 1

            if elv.state == 'stop' and elv.y_goal != None and elv.filling == 1:
                # print('remained stop door and passenger time:', elv.t_door_psg)
                for justArrivedPsg in waiting_list:
                    elv.passengers.append(justArrivedPsg)
                    elv.t_door_psg += t_psg
                    waiting_list.remove(justArrivedPsg)
                    if ((elv.y_goal > elv.y_begin) and (justArrivedPsg.y2 > elv.y_goal)) or ((elv.y_goal < elv.y_begin) and (justArrivedPsg.y2 < elv.y_goal)):
                        # print('working')
                        elv.y_goal = justArrivedPsg.y2

                elv.t_door_psg -= dt



    # @staticmethod
    # def elevator_travelling_update(elevator, v_ave, dt):
    #     if elevator.y < elevator.y_goal:
    #         elevator.state = 'moving'
    #         elevator.y += dt * v_ave
    #     elif elevator.y >= elevator.y_goal:
    #         elevator.y = elevator.y_goal
    #         elevator.state = 'stop'






    @staticmethod
    def updateStates(elevators):
        for elv in elevators:
            if elv.state == 'idle':
                # calling idle elevator
                if elv.y_goal != None:
                    if elv.y_goal > elv.y_begin:
                        elv.state = 'moving'
                        elv.movingDir = 1
                    elif elv.y_goal < elv.y_begin:
                        elv.state = 'moving'
                        elv.movingDir = -1
                    elif elv.y_goal == elv.y_begin:
                        elv.state = 'stop'
                        elv.y_goal = None
                        elv.filling = 1
                        # print('this')
                        # print(elv.state, elv.y_goal)
            elif elv.state == 'moving':
                if (elv.movingDir == 1 and elv.y_inst >= elv.y_goal) or (elv.movingDir == -1 and elv.y_inst <= elv.y_goal):
                    elv.state = 'stop'
                    elv.y_begin = elv.y_goal
                    elv.y_goal = None
                    elv.filling = 1
                    elv.y_inst = elv.y_begin


            ############# elv stop time should be added here later #############
            elif elv.state == 'stop':
                print('causing problem:', 'id:', elv._id, elv.passengers, elv.state, elv.filling, elv.t_door_psg)
                if elv.y_goal == None and elv.filling == 0:
                    elv.state = 'idle'



                elif elv.y_goal != None:
                    if elv.t_door_psg <= 0:
                        elv.filling = 0
                        elv.state = 'moving'












