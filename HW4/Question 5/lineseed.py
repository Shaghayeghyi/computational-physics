import random
import numpy as np
import matplotlib.pyplot as plt

#we need to create a plane
width=200
height=100
start_height=90
grid=np.zeros((height,width))
#initial seed
grid[0,:]=1

#print(grid)

#now we will send RW down from a height like 200 as a test

def random_walk2(x,y):
    
    rand = random.random()

    if rand < 1/4:
        #right
        x+=1      
    elif rand < 2/4:   
        #up
        y+=1
    elif rand < 3/4:   
        #down
        y-=1    
    else:    
        #left
        x-=1

            
    return x,y

#i want the RW continue till it gets stuck or gets out of range

#i need a function that checks all the neighbors of the target site to see whether a merging will happen.


def will_it_merge(x,y, grid):
    
    four_moves=[(1,0),(0,1),(-1,0),(0,-1)]
    for m,n in four_moves:
        xneighbor=(x+m)%width
        yneighbor=y+n
        if 0 <= yneighbor < height and grid[yneighbor, xneighbor] != 0:
            return True #yes it will stick
    return False #no i did not stick
            
        
#test particles
particles=2000

for i in range(particles):
    
    x_start=random.randint(0, width-1)
    y_start=start_height
    x=x_start
    y=y_start
    color = 1 + (i // 500) * 10 
    
    while True:
        
        #start walking
        x,y=random_walk2(x,y)
        x=x%width
        
        
        if y >= height or y < 0:
            #restart the process forget the past
            x = random.randint(0, width - 1)
            y = start_height
            continue
        
        
        if will_it_merge(x,y,grid):
            grid[y,x]=color
            break
            
        '''
        #bad idea
        if i%500==0:
            color+=10'''
        

'''plt.imshow(grid, cmap='nipy_spectral') 
plt.title('DLA Simulation with Initial Line Seed')
plt.show()  '''

plt.pcolor(grid , cmap ='nipy_spectral')

    
    



    
