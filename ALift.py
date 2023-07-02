import math

fl_dist = 4 # floor distance
cap = 24 # each elevator capacity
t_door = 1.5 # door time
t_psg_geton = 1.5 # passenger time
v_max = 2.5 # maximum velocity
a_max = 1 # maximum acceleration
j_max = 2 # maximum jerk


class Elevator:
    def __init__(self, _id, cpty = 20, state='idle', y_begin=0, y_goal=None, movingDir=0, y_inst=0, passengers=[], t_door_psg=None, filling=0): # filling == 1 : picking up, filling == -1 : dropping off
        # movingDir = 0: idle, 1: up, -1: down
        self.cpty = 20
        self.state = state
        self.y_begin = y_begin
        self.y_goal = y_goal
        self.movingDir = movingDir
        self.y_inst = y_inst
        self.passengers = passengers
        self.t_door_psg = t_door_psg
        self.filling = filling
        self._id = _id

    def calculateFS(self, N, yPassenger, landingCall):
        FS = 0
        d = abs(self.y_inst - yPassenger)
        # print('#', self._id, 'y instant:', self.y_inst, 'd:', d)

        if (yPassenger == 0 and landingCall == -1) or (yPassenger == N and landingCall == 1):
            ##        print('state 0')
            return None

        if (self.y_inst >= yPassenger and self.movingDir == -1 and landingCall == -1) or (self.y_inst <= yPassenger and self.movingDir == 1 and landingCall == 1):
            ##        print('satate 1')
            FS = N + 2 - d
        elif (self.y_inst >= yPassenger and self.movingDir == -1 and landingCall == 1) or (self.y_inst <= yPassenger and self.movingDir == 1 and landingCall == -1):
            ##        print('state 3')
            FS = N + 1 - d
        elif self.movingDir == 0:
            ##        print('satate 4')
            FS = N + 1 - d
        elif (self.y_inst > yPassenger and self.movingDir == 1) or (self.y_inst < yPassenger and self.movingDir == -1):
            ##        print('state 5')
            FS = 1

        return FS

    def travel(self, dt):
        d = abs(self.y_goal - self.y_begin)
        if d > 0:
            high_value = (a_max ** 2 * v_max + v_max ** 2 * j_max) / (j_max * a_max)
            low_value = 2 * a_max ** 8 / (j_max ** 2)
            # print('***********\n', 'high:', high_value, 'low:', low_value, 'd:', d)

            if d >= high_value:
                t_tr = (d/v_max) + (a_max/j_max) + (v_max/a_max)
                # print('travel time: "high value"')
            elif d >= low_value:
                t_tr = (a_max/j_max) + math.sqrt(a_max**3 + 4*d*j_max**2) / math.sqrt(a_max*j_max)
                # print('travel time: "between value"')
            else:
                t_tr = (32 * d / j_max) ** (1./3.)
                # print('travel time: "low value"')
            v_ave = d / t_tr

            if self.y_goal > self.y_begin:
                self.movingDir = 1
                self.y_inst += dt * v_ave
            elif self.y_goal < self.y_begin:
                self.movingDir = -1
                self.y_inst -= dt * v_ave







