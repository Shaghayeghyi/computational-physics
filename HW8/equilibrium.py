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
@jit(nopython=True)
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

#we need to define functions for energy of lattice, m , Cv , X and correlation lenght

@jit(nopython=True)
def energy(lattice, L, J):
    sum_of_neighbors=0
    for i in range(L):
        for j in range(L):
            S_ij=lattice[i,j]
            sum_of_neighbors+=(S_ij*(lattice[(i-1)%L,j]+lattice[(i+1)%L,j]+lattice[i,(j-1)%L]+lattice[i,(j+1)%L]))
    energy=-J*(sum_of_neighbors /2)
    return energy


def m(lattice,L):
    sums=0
    for i in range(L):
        for j in range(L):
            sums+=lattice[i,j]
    #in unit of volume
    return sums/(L**2)


def specific_heat(energies, T):
    energies = np.array(energies)  
    mean_energy = np.mean(energies)
    energy_squared_mean = np.mean(energies**2) 
    specific_heat = (energy_squared_mean - mean_energy**2) / (T**2)
    return specific_heat
    
def susceptibility(M, T):
    M = np.array(M)
    X_mean = np.mean(M)
    X_2 = np.mean(M**2) 
    X = (X_2 - X_mean**2) / T 
    return X

def correlation(array,j):
    n=len(array)
    sigma=np.var(array)
    sum_ij=0
    sum_j=0
    for i in range(n-j):
        sum_ij+=array[i]*array[i+j]
        sum_j+=array[i+j]
    mean_ij=sum_ij/(n-j)
    mean_j=sum_j/(n-j)
    lenght_j=(mean_ij-np.mean(array)*mean_j)/sigma
    return lenght_j
    
def Jss(J0, a, steps):
    Js = [J0]
    for _ in range(steps - 1):
        Js.append(Js[-1] * a)
    return np.array(Js)

     
def main_part(X,J,L):
    lattice = Lattice(L)
    Ms = []
    Es = []
    steps = []
    for i in range (X):
        lattice_final = metropolis(lattice ,L,J) 
        Ms.append(m(lattice_final,L))
        Es.append(energy(lattice_final,L,J))
        steps.append(i)         
          
    return  steps , Es , Ms 
J=2
X=35000
L=50
#running the whole part 10 times to find the best sweep number    
colors = ['b','r','g','c','m','y','k','orange','deeppink','greenyellow']    
for j in range (1):
    step,E,M = main_part(X,J,L)
    fig = plt.figure(figsize=(15, 5))
    plt.xlabel("sweep")
    plt.ylabel("M")
    plt.plot(step,M,color = colors[j] )
    plt.show()
    fig = plt.figure(figsize=(15, 5))
    plt.xlabel("sweep")
    plt.ylabel("E")
    plt.plot(step,E,color = colors[j])
    plt.show()
        

