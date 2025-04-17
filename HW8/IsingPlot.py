#we will try to @jit to make our code faster as Alireza explained :)
import numpy as np
import matplotlib.pyplot as plt
import random
from numba import jit

#creating the initial lattice
@jit(nopython=True)
def Lattice(L):
    #get 0 1, then map to -1 and 1 this is supported by jit
    rand_array = np.random.randint(0, 2, size=(L, L))
    lattice = 2 * rand_array - 1
    return lattice

#check
#lattice=Lattice(50)

#save the energy change for a filp in (i,j)!
@jit(nopython=True)
def delta_E(lattice,i,j,L,J):
    #periodic boundary
    delta=-2*J*lattice[i,j]*(lattice[(i-1)%L,j]+lattice[(i+1)%L,j]+lattice[i,(j-1)%L]+lattice[i,(j+1)%L])
    return delta
#the out puts seeem to be correct accodrgin to book
#print(delta_E(lattice,0,1,10,1))
