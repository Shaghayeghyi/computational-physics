import random
import numpy as np
import matplotlib.pyplot as plt

#i want to find every possible SAW with a lenght N and plot the results
#we will make it recursive and the output will be the count
def all_SAW(N,x,y):
    count=0
    # i will create a grid
    plane=np.zeros((2*N,2*N))
    if N==0:
        return 1 #only one way possible
    else:
        plane[x,y]=1 #visited
        shifts=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
        #if the neighbors are not vistied then we need to check all of them
        for shift in shifts:
            new_posx, new_posy=shift
            if plane[new_posx,new_posy]!=1: #not visited
                count+=1
                

    
