import numpy as np
import matplotlib.pyplot as plt
from random import random,randint

#at first we need to create a LxL lattice full of zeros
#then we will assing a random number betwwen (0,1) to each house
def random_on(L,p):
    Lattice=np.zeros((L, L), dtype=int)
    random_p=np.random.rand(L, L)
    #go through lattice
    for i in range(L):
        for j in range(L):
            if random_p[i,j]<p:
                Lattice[i,j]=1
            else:
                Lattice[i,j]=0
    return Lattice
            
'''plt.imshow(random_on(2,0.5))
plt.show()'''
#for seeing whether the percolation happend or not, we will start from on sites and the left
#for each one we will look at the top, down and right neighbor for a path
#after visiting each site, we will marke it to not go through that again
#by moving to right and reaching the very right column with number one, we will assume that the percolation happened

def find_path(Lattice):
    L=3
    p=0.5
    left_column=random_on(L,p)[:,0]
    #not seen sites are zero
    paths=np.zeros((L, L), dtype=int)
    for i in range(L):
        for j in range(L):
            
    
