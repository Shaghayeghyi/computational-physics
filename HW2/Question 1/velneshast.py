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
N_sample=20000

