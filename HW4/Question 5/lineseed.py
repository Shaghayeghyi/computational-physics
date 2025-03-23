import random
import numpy as np
import matplotlib.pyplot as plt

#we need to create a plane
width=200
height=220
grid=np.zeros((width,height))
#initial seed
grid[-1,:]=1

#print(grid)

#now we will send RW down from a height like 200 as a test

def random_walk2(current_position):
    
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

            
    return current_position
