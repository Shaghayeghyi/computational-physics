import random
import numpy as np
import matplotlib.pyplot as plt

#we need to create a plane
width=210
height=210
grid=np.zeros((height,width))
#initial seed is in center now
x_c=int(width/2)
y_c=int(height/2)
grid[int(height/2),int(width/2)]=1
#print(grid)
maxr=100
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
        xneighbor=x+m
        yneighbor=y+n
        if 0 <= xneighbor < width and 0 <= yneighbor < height:
             if grid[yneighbor, xneighbor] != 0:
                return True #yes it will stick
             
    return False #no i did not stick
            
        
#test particles
particles=2000
def initial_circle(x_c,y_c,radius):
    initials=[]
    #number of positions
    num=100
    angles = np.linspace(0, 2 * np.pi, num, endpoint=False)
    x_on_circle= x_c + np.round(radius * np.cos(angles)).astype(int) 
    y_on_circle = y_c + np.round(radius * np.sin(angles)).astype(int)
    #initials.append(( x_on_circle ,y_on_circle))
    return list(zip(x_on_circle, y_on_circle))


for i in range(particles):
    #randomly choose on a circle with radius r
    radius=95
    x_start, y_start=random.choice(initial_circle(x_c,y_c,radius))
    x=x_start
    y=y_start
    color = 1 
    
    while True:
        
        #start walking
        x,y=random_walk2(x,y)
    
    
        if ((x-x_c)**2+(y-y_c)**2)>maxr**2:
            x_start, y_start=random.choice(initial_circle(x_c,y_c,radius))
            x=x_start
            y=y_start
            continue
        
        
        if will_it_merge(x,y,grid):
            grid[y,x]=color
            break
            
    
        

'''plt.imshow(grid, cmap='nipy_spectral') 
plt.title('DLA Simulation with Initial Line Seed')
plt.show()'''


plt.pcolor(grid , cmap ='nipy_spectral')

   
    



    
