import numpy as np
import random as r
import matplotlib.pyplot as plt
#we will be working onsome simple 1D surface growth process
#at first we need to create a surface on the x axis say with a lenght of 200
x=np.arange(0,200,1)
#print(x)
#now we need to create an array of length 200 to save the height of each x
#this is a 1D array to save the height which is 0 at first
height=np.zeros(200)
#we will also need a number of samples that will fall on the surface
N_samples=20000

#we need a for loop to go through every sample and find a place for it
time_splitted_sample=[]
for i in range(N_samples):
    if i==int(N_samples/4):
        time_splitted_sample.append(height.copy())
    if i==2*int(N_samples/4):
        time_splitted_sample.append(height.copy())
    if i==3*int(N_samples/4):
        time_splitted_sample.append(height.copy())
    if i==N_samples-1:
        time_splitted_sample.append(height.copy())
    #the question wants us to split our deposition into 4 differen timelines
    #so we will save each quarter of samples in a array
    rand_house=r.randint(0,199)
    #add a unit to the height of rand_house
    height[rand_house]=height[rand_house]+1
    
    
#print(x)
plt.bar(x,time_splitted_sample[0], color='blue',alpha=0.6)
plt.bar(x,time_splitted_sample[1], color='red',alpha=0.6)
plt.bar(x,time_splitted_sample[2], color='blue',alpha=0.6)
plt.bar(x,time_splitted_sample[3], color='red',alpha=0.6)

plt.show()
