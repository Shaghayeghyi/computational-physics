import numpy as np
import matplotlib.pyplot as plt
from random import random,randint
#we want to look at pecolation using HK algorithm
#we have a top left check system so we will get rid of on row and column
#we need an array so save the size of clusters
#we need a plane LxL
#we should create a function that leads us to the root:)
L=10
p=0.3
plane = np.zeros((L,L+2),dtype = int)#L+2 for side's column
plane[:,0]=1
plane[:,-1]=100
count=0
for j in range(1,L):
    for i in range(1,L):
        random_p=random()
        if random_p<p:
            plane[i,j]=1
            count=count+1
            #creating the grid and counting the number of on sites
#print(plane)
        





