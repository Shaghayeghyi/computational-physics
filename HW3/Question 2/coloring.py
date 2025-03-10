import numpy as np
import matplotlib.pyplot as plt
from random import random,randint
#we wnat to simulate percolation using coloring methods
#we have a LxL lattice once again but the most lef and right column have initial values:

def lattice(L,p):
    #create 2D array with all zeros at first
    plane=np.zeros((L,L))
    #give number 1 to the left column
    left_column=plane[:,0]=1
    int_max=100
    right_colimn[:,L-1]=int_max
    #now lets check every house
    for i in range(1,L-1):
        for j in range(1,L-1):
            
