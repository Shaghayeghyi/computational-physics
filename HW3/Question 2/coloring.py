import numpy as np
import matplotlib.pyplot as plt
from random import random,randint
#we want to simulate percolation using coloring methods
#we have a LxL lattice once again but the most lef and right column have initial values:

def lattice(L,p):
    color=2
    #create 2D array with all zeros at first
    plane=np.zeros((L,L))
    #give number 1 to the left column
    left_column=plane[:,0]=1
    int_max=100
    right_column[:,L-1]=int_max
    #now lets check every house
    for i in range(1,L-1):
        for j in range(1,L-1):
            random_p=random.random()
            if random_p<p:
                plane[i,j]=color
                color=color+1
                #so we have a different color for the other houses
                #up down right
            neighbors=[(i-1,j),(i+1,j),(i,j+1)]
            #we want the non zero neighbors
            for m,n in neighbors:
                non_zero_neighbors=[]
                if plane[m,n]!=0:
                    non_zero_neighbors.append((m,n))
            '''if len(non_zero_neighbors)==0:
                 #no non zero neighbors'''
                
            if len(non_zero_neighbors)==1:
                lattice[non_zero_neighbors[0]]=plane[i,j]
            elif len(non_zero_neighbors)==2:
                min_housex, min_housey =min(plane[non_zero_neighbor[0]],plane[non_zero_neighbor[0]])
                plane[i,j]=plane[min_housex, min_housey]
                
            
            
