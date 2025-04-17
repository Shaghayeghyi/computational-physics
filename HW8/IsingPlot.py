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
    #boundary
    delta=2*J*lattice[i,j]*(lattice[(i-1)%L,j]+lattice[(i+1)%L,j]+lattice[i,(j-1)%L]+lattice[i,(j+1)%L])
    return delta
#the outputs seeem to be correct according to book
#print(delta_E(lattice,0,1,10,1))


#now let's define the metropolis loops
def metropolis(lattice,L,J):
    #we want to check the energy change by going through a random choice of i,j 
    for iteration in range(L*L):
        i=np.random.randint(0,L)
        j=np.random.randint(0,L)
        dE=delta_E(lattice,i,j,L,J)
        if dE <= 0 or np.random.rand() < np.exp(-dE):
            lattice[i, j] *= -1
            
    return lattice
#metropolis(lattice,50,2)


#we can check our code for critical behavior
Js=[1,2,3,4,5]
time_steps=100
#in a for loop create the animations of evolutions
for J in Js:
    #evolution for each J will be stored in a 3D array
    lattice_snapshot=np.zeros((time_steps,L,L))
    lattice=lattice(L)
    for time in range(time_steps):
        
        



