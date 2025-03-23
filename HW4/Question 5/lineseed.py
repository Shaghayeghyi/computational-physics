import random
import numpy as np
import matplotlib.pyplot as plt

#we need to create a plane
width=200
height=210
start_height=200
grid=np.zeros((width,height))
#initial seed
grid[-1,:]=1

#print(grid)

#now we will send RW down from a height like 200 as a test

def random_walk2(current_position):
    
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

#i want the RW continue till it gets stuck or gets out of range

#i need a function that checks all the neighbors of the target site to see whether a merging will happen.


def will_it_merge(x,y):
    four_moves=[(1,0),(0,1),(-1,0),(0,-1)]
    for m,n in four_moves:
        xneighbor=x+m
        yneighbor=y+n
        if grid[xneighbor, yneighbor]!=0
            return 1 #yes it will stick
    return 0 #no i did not stick
            
        
#test particle
x_start=random.randint(0, width-1)
y_start=start_height
x=x_start
y=y_start
color=10                
while True:
    #start walking
    x,y +=random_walk2((x,y))

    if will_it_merge:
        grid[x,y]=color
        
    elif not will_it_merge:
        break
    

    

    
    



    
