import numpy as np

from passengerArrival import individualPassengersArrival
from passenger import Passenger
from ALift import Elevator
from scheduler import Scheduler


# simulation, building and elevator characteristics
lam = 0.4
n_floors = 20 # number of floors
n_elvs = 6
systemTime = 0 # system time
dt = 0.01 # delta t - time raising value
simTime = 3600 # simulation time
yPassenger = 0 # where the passenger will get on the elevator


# create passengers for individual Poisson arrival
passengers, t_indiv_arrivals = individualPassengersArrival(Passenger, lam, WS=simTime, n_floors=n_floors, y1=yPassenger)

f = open('result-60.txt', 'w')
for psg in passengers:
    f = open('result-60.txt', 'a')
    f.write('passenger#{:5} | arrival time:{:8} | destination: {}\n'.format(psg._id, psg.arrTime, psg.y2))
    print('passenger#{} | arrival time:{} | destination: {}'.format(psg._id, psg.arrTime, psg.y2))

f.write('+++++++++++++++++++++++++++++++++++++++++++\n')


# print('arrival times:', t_indiv_arrivals)

# # test the creation of passengers
# for passenger in passengers:
#     print(passenger._id)

# create elevators
elevators = []
for i in range(0, n_elvs):
    newEl = Elevator(_id=i)
    elevators.append(newEl)

# # test the creation of elevators
# for elv in elevators:
#     print(elv._id)


def startSimulation():
    systemTime = 0  # system time
    dt = 0.01  # delta t: time raising value
    updatedIntervals = list(t_indiv_arrivals)
    waiting_list = []

    while systemTime <= simTime:

        f = open('result-60.txt', 'a')
        waitingPassenger = [psg for psg in passengers if psg.arrTime == systemTime]

        if len(waitingPassenger) > 0:
            waiting_list.extend(waitingPassenger)

        # print('waiting list:', waiting_list)
        # for psg in waiting_list:
        #     print('passenger#{} | arrival time:{}'.format(psg._id, psg.arrTime))


        # if a passenger has arrived (waitingPassenger exists) we should first find the best landig car
        Scheduler.selectElevators(waiting_list, elevators)

        # update the postition of moving elevators
        Scheduler.moveElevators(elevators, dt)

        # takeoff passenger
        Scheduler.dropoff_passengers(elevators, dt)

        # pickup_passengers
        Scheduler.pickup_passengers(elevators, waiting_list, dt)



        Scheduler.updateStates(elevators)

        if systemTime <= simTime:
            f.write('system time: {}\n'.format(systemTime))
            f.write('elv #{} | state: {} | passengers: {} | y_begin: {} | y_goal: {} | y: {} | remainig: {} | filling {}\n'.format(elevators[0]._id, elevators[0].state, elevators[0].passengers, elevators[0].y_begin, elevators[0].y_goal, elevators[0].y_inst, elevators[0].t_door_psg, elevators[0].filling))
            f.write('==============================\n')
            print('system time:', systemTime)
            # print('elv #{} | state: {} | passengers: {} | y_goal: {} | y: {} '.format(elevators[0]._id, elevators[0].state, elevators[0].passengers, elevators[0].y_goal, elevators[0].y_inst))
            # print('==============================')
        f.close()
        # for elv in elevators:
        #
        #     print('elv #{} | state: {} | passengers: {} | y: {}'.format(elv._id, elv.state, elv.passengers, elv.y_inst))





        # updatedIntervals = [arr for arr in updatedIntervals if arr >= systemTime]
        systemTime = round(systemTime + dt, 2)


startSimulation()





print('end')