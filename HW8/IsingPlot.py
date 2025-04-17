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
L=50
Js=[0.4, 0.45, 0.5, 0.55, 0.6]
time_steps=100
evolution_for_Js=[]
#in a for loop create the animations of evolutions
for J in Js:
    #evolution for each J will be stored in a 3D array
    lattice_snapshot=np.zeros((time_steps,L,L))
    lattice=Lattice(L)
    for time in range(time_steps):
        lattice=metropolis(lattice,L,J)
        lattice_snapshot[time]=lattice
    evolution_for_Js.append(lattice_snapshot)


#animation
import matplotlib.animation as animation
import matplotlib
from IPython.display import HTML
for idx, J in enumerate(Js):
    data = lattices_per_J[idx]

    fig, ax = plt.subplots()
    im = ax.imshow(data[0], cmap='bwr', vmin=-1, vmax=1)
    ax.set_title(f'Ising Model: J = {J}')
    ax.axis('off')

    def update(frame):
        im.set_array(data[frame])
        return [im]

    ani = animation.FuncAnimation(fig, update, frames=time_steps, interval=100, blit=True)
    display(HTML(ani.to_jshtml()))
    plt.close()






