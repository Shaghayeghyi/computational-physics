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
            
plt.imshow(random_on(2,0.5))
plt.show()
