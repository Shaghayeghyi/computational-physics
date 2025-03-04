import numpy as np
import matplotlib.pyplot as plt
import random as r
#we will define the surface at first
N_samples=2000
L = 200
x = np.arange(0,L,1)
#we can have a 2D array too
height_map = np.zeros((grid_height, width))
#we need to save the height
height = np.zeros(L)
#now lets go through samples
for i in range(N_samples):
    #choose a house initially
    r_house= r.randint(0, L - 1)
    
    for j in range(r_house):
        #check every house on the left
        #assume the particle falls leftward
        #we must check the height of every single room at the left of the index
        #i also assume that the angle is 45 degree so i move diagonal 
   



plt.bar(x , height)
plt.xlabel('Position')
plt.ylabel('Height')
plt.show()
