import numpy as np
import matplotlib.pyplot as plt
import random as r
#we will define the surface at first
N_samples=2000000
L = 200
x = np.arange(0,L,1)
#we can have a 2D array too
height_map = np.zeros((2000, L))
#we need to save the height
height = np.zeros(L)
#now lets go through samples
'''deg=np.radians(45)
horizantal_shift=np.round(np.sin(deg))
vertical_shift=np.round(np.cos(deg))
print(horizantal_shift,vertical_shift)'''

'''collide=False
for i in range(N_samples):
    #choose a house initially
    r_house= r.randint(0, L - 1)
    #so my system starts at the left neighbor, goes aroung and reches the right neighbor
    moving_sys = [(r_house - k) % L for k in range(1, L)]

    for j in moving_sys:
        j=()
        #check every house on the left
        #assume the particle falls leftward
        #we must check the height of every single room at the left of the index
        #i also assume that the angle is 45 degree so i move diagonal
        #i want to be careful about negatives in periodic boundaries
        horizontal_d = min(abs(r_house - j), L - abs(r_house - j))
        #for simplicity i assume that if the height(r_house) itself is the max, the particle lands there
        #if it doesn't it must collide with a column of its left
        #the h where the sample falls from
        height1=1000
        if height1<height[j]+horizontal_d:
            #this is a pattern that i saw
            height[j]+=1
            collide=True
            #the collision with column j happened we are out
            break
        else:
            continue
            #move to the next column and check collision
        if not collide:
            height[r_house] += 1 
print(height) 

plt.figure(figsize=(10, 5))
plt.bar(x , height,width=1)
plt.xlabel('Position')

plt.ylabel('Height')
plt.show()'''
import numpy as np
import matplotlib.pyplot as plt
import random as r
#we will define the surface at first
N_samples=1000
L = 100
x = np.arange(0,L,1)
#we can have a 2D array too
height_map = np.zeros((2000, L))
#we need to save the height
height = np.zeros(L)
#now lets go through samples
'''deg=np.radians(45)
horizantal_shift=np.round(np.sin(deg))
vertical_shift=np.round(np.cos(deg))
print(horizantal_shift,vertical_shift)'''
collide=False
for i in range(N_samples):
    #choose a house initially
    r_house= r.randint(0, L - 1)
    #initial height
    height1=1000
    #now we work on the dynamic of each particle
    while height1>0:
        #starting point r_house
       
        if height1<=height[r_house]:
            height[r_house]+=1
            #it doesnt happen at the first step
            break
        #move leftward
        r_house=(r_house-1)%L
        #decrease the height
        height1=height1-1
        if height1==0:
            #no collision just put it one the surfaace
            height[r_house]+=1
       
plt.figure(figsize=(10, 5))
plt.bar(x , height,width=1)
plt.xlabel('Position')

plt.ylabel('Height')
plt.show()
    
