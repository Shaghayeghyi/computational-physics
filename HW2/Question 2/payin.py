import numpy as np
import random as r
import matplotlib.pyplot as plt
#now we will work with some interaction with neighbors
#again we have a 1D surface
x=np.arange(0,200,1)
#for each house we need to determine the height
height=np.zeros(200)
#we also need a time_snap to save the dynamic after a certain amount of time
N_samples=200000
height_snapshot=[]
time_snapshot=[100,1000,10000,100000, N_samples-1]

for i in range(N_samples):
    #choose a house
    rand_house=r.randint(0,199)
    #check the neighbors
    #we have 200 houses, the house at 0 and 200 should be neighbours. for this we have to link 0 and 199 with a periodic boundary.
    #module cam do this for us easily because it has affect on the two end houses naturally
    #print(-1%200) is 199 wich is corrrect!
    #for 199=> 200%200 is 0 which is correct again :)
    minimum_height=min(height[rand_house],height[(rand_house+1)%200],height[(rand_house-1)%200])
    minimum_height=minimum_height+1
    #now lets save snap shots!
    for j in time_snapshot
