import numpy as np
import matplotlib.pyplot as plt
from random import randint,random

#simulating random walk
def random_walk(P)

    p=P
    q=1-p
    start_point=0
    current_position=0
    positions=[]
    positions.append(start_point)
    position_copy=[]
    iteration=1000
    for i in range(len(iteration)):
        rand = random()
        #right and left
        if rand < p:
            current_position=current_position+1
        else:
            current_position=current_position-1
            
        positions.append(current_position)
         if i%100==0: #make a copy
             position_copy.append(positions.copy())
             
    averag=[]
    Std=[]
    for j in range(len(positions_copy))
        averag.append(np.mean(positions_copy[j]))
        Std.append(np.std(positions_copy[j]))
    
    return averag, Std
#average and Std of position
   

