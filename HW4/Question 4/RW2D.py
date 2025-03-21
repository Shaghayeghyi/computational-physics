import numpy as np
import matplotlib.pyplot as plt
from random import randint,random

#simulating random walk in 2D
from random import random

def random_walk2(P=0.25):
    current_position = (0, 0)
    position_copy = []

    iteration = 100
    for i in range(iteration + 1):
        rand = random()

        if rand < 1/4:
            #right
            current_position = (current_position[0] + 1, current_position[1])  
            
        elif rand < 2/4:
            
            #up
            current_position = (current_position[0], current_position[1] + 1)
        elif rand < 3/4:
            
            #down
            current_position = (current_position[0], current_position[1] - 1) 
            
        else:
            
            #left
            current_position = (current_position[0] - 1, current_position[1])  

        if i % 10 == 0:
            position_copy.append(current_position)
            
    return position_copy
#lets run this code for 100 times

