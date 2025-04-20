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


#main code, we are ready use our functions
def main_function(run,L,sample_step,corr_lag):
    Js = np.linspace(0.2, 1.0, 20)
    #do this at different Ts or equivalently Js
    T_energies=[]
    T_magnetism=[]
    T_Cv=[]
    T_chi=[]
    #T_correlations=[]
    for J in Js:
        energies=[]
        magnetism=[]
        #correlations=[]
        lattice=Lattice(L)
        
        for runs in range(run):
            #forget intial condition, look for equilibrium
            lattice=metropolis(lattice,L,J)
        lattice_final=lattice
        
        for sample in range(sample_step):
            latt = metropolis(lattice_final,L,J)
            energies.append(energy(latt,L,J))
            magnetism.append(m(latt,L))
            
        #we have no h
        T = 1.0 / J
        avg_energy = np.mean(energies)
        avg_magnet = np.mean(np.abs(magnetism))
        cv = specific_heat(energies, T)
        chi = susceptibility(np.abs(magnetism), T)
        #corr = correlation(magnetism, corr_lag)
        T_energies.append(avg_energy)
        T_magnetism.append(avg_magnet)
        T_Cv.append(cv)
        T_chi.append(chi)
        #T_correlations.append()
    return Js, T_energies, T_magnetism, T_Cv,T_chi

Js, T_energies, T_magnetism, T_Cv,T_chi=main_function(10,10,1000,10)
T = 1.0 / np.array(Js)


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes[0, 0].scatter(T,T_energies )
axes[0, 0].set_title('E-T')
axes[0, 0].set_xlabel("T")
axes[0, 0].set_ylabel("E")

axes[0, 1].scatter(T, T_magnetism)
axes[0, 1].set_title('M-T')
axes[0, 1].set_xlabel("T")
axes[0, 1].set_ylabel("M")

axes[1, 0].scatter(T, T_Cv)
axes[1, 0].set_title('C-T')
axes[1, 0].set_xlabel("T")
axes[1, 0].set_ylabel("C")

axes[1, 1].scatter(T, T_chi)
axes[1, 1].set_title('X-T')
axes[1, 1].set_xlabel("T")
axes[1, 1].set_ylabel("X")
 

