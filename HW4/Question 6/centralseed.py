import random
import numpy as np
import matplotlib.pyplot as plt
#circle
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
    num=12
    angles = np.linspace(0, 2 * np.pi, num, endpoint=False)
    x_on_circle= x_c +(radius * np.cos(angles)).astype(int)
    y_on_circle = y_c +(radius * np.sin(angles)).astype(int)
    #initials.append(( x_on_circle ,y_on_circle))
    return list(zip(x_on_circle, y_on_circle))

radius=95
'''
#check
points=initial_circle(0,0,10)
plt.scatter(*zip(*points), color='red', s=50)
plt.axis('equal')
plt.show()'''
for i in range(particles):
    #randomly choose on a circle with radius r
    x_start, y_start=random.choice(initial_circle(x_c,y_c,radius))
    x=x_start
    y=y_start
    color = 1 
    index=True
    while index:
        
        #start walking
        x,y=random_walk2(x,y)
        R=(x-x_c)**2+(y-y_c)**2
    
        if (R)>maxr**2:
            x, y=random.choice(initial_circle(x_c,y_c,radius))
            #print(x,y) 
            continue
        
        
        if will_it_merge(x,y,grid):
            #just in case check this
            if 0 <= x < width and 0 <= y < height:
                grid[y, x] = 1
                index = False
            
    
        
plt.figure(figsize=(5, 5))
plt.imshow(grid, cmap='Grays',origin='lower') 
plt.title('DLA Simulation with central Seed')
plt.axis('equal')
plt.show()


#plt.pcolor(grid , cmap ='nipy_spectral')

 
    



    
