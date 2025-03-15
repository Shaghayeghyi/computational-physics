import numpy as np
import matplotlib.pyplot as plt
from random import random,randint

#we will start by a plane and a seed in the middle
plane = np.zeros((L,L),dtype = int)
middle=int(L/2)
#turn it on
activation=(middle,middle)
plane[middle,middle]=1

neighbors=[activation]
null=[]


while neighbors!=null:
    
    i,j=neighbors.pop()
    all_four_sides=[(i-1,j),(i,j-1),(i+1,j),(i,j+1)]
    #we will only work with on sites
    for k,l in all_four_sides:
        
    

