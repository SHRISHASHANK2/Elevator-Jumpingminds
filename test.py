import numpy as np
import random as random
import math

U = 300

lam = 0.04 * U / (5 * 60)
WS = 15 * 60
b = (37 * 1 + 13 * 2 + 6 * 3 + 2 *4) / 58

lam_b = lam / b
print(lam_b)

batch_gen = WS * lam_b

arrivals = []

def delta_t():
    return -np.log(1 - random.random()) / lam_b


new_a = delta_t()

while len(arrivals) <= batch_gen:
    arrivals.append(new_a)
    new_a = new_a + delta_t()
    

FS = WS / new_a
arrivals.pop()
arrivals = np.array(arrivals)

arrivals = FS * arrivals

print(arrivals)
    
    


