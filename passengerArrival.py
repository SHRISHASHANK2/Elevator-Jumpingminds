import numpy as np
import random

# creating individual passenger using individual Possion passenger
def individualPassengersArrival(Passenger, lam, WS, n_floors, y1):
    p_gen = lam * WS
    print('p_gen: ', p_gen)
    individualArrivals = []
    newArrival = 0
    passengers = []

    while len(individualArrivals) <= p_gen:
        individualArrivals.append(newArrival)
        delta_t = -np.log(1 - random.random()) / lam
        newArrival = newArrival + delta_t

    sf = WS / individualArrivals.pop()

    individualArrivals = np.array(individualArrivals)
    individualArrivals = np.round(sf * individualArrivals, 2)
    # print(individualArrivals, p_gen)

    i = 0
    for arrival in individualArrivals:
        y2 = random.randint(1, n_floors)
        newPass = Passenger(arrTime=arrival, y1=y1, y2=y2, _id=i)
        passengers.append(newPass)
        i = i + 1

    return passengers, individualArrivals

