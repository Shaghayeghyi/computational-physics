#we will try to @jit to make our code faster as Alireza explained :)
import numpy as np
import matplotlib.pyplot as plt
import random
from numba import jit
from scipy.optimize import curve_fit

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
def delta_E(lattice,i,j,L):
    #boundary
    delta=2*lattice[i,j]*(lattice[(i-1)%L,j]+lattice[(i+1)%L,j]+lattice[i,(j-1)%L]+lattice[i,(j+1)%L])
    return delta
#the outputs seeem to be correct according to book
#print(delta_E(lattice,0,1,10,1))


#now let's define the metropolis loops
@jit(nopython=True)
def metropolis(lattice,L,T):
    #we want to check the energy change by going through a random choice of i,j 
    for iteration in range(L*L):
        i=np.random.randint(0,L)
        j=np.random.randint(0,L)
        dE=delta_E(lattice,i,j,L)
        if dE <= 0 or np.random.rand() < np.exp(-dE/T):
            lattice[i, j] *= -1
            
    return lattice
#metropolis(lattice,50,2)

#we need to define functions for energy of lattice, m , Cv , X and correlation lenght

@jit(nopython=True)
def energy(lattice, L):
    sum_of_neighbors=0
    for i in range(L):
        for j in range(L):
            S_ij=lattice[i,j]
            sum_of_neighbors+=(S_ij*(lattice[(i-1)%L,j]+lattice[(i+1)%L,j]+lattice[i,(j-1)%L]+lattice[i,(j+1)%L]))
    energy=-1*(sum_of_neighbors /2)
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
    
def correlation(lattice,L):
    mean_spin = np.mean(lattice)
    var_spin = np.var(lattice)
    
    if var_spin == 0:
        #fully ordered, we have to definition
        return 0  

    
    max_shift =int(L/4)
    mean_products = []
    C_shift=[]
    for shift in range(max_shift):
        #shift the latice by column
        rolled = np.roll(lattice, shift , axis=1)
        mean_products.append(np.mean(rolled*lattice))
    
    C_shift=(np.array(mean_products) - mean_spin**2) / var_spin
    #C_shift=C_shift/(L*L)
    
    
    



    #fit
    def exp_decay(shift, a, ksi):
        return a * np.exp(-shift / ksi)

    shifts= np.arange(max_shift)

    a_ksi, _ = curve_fit(exp_decay, shifts, C_shift, p0=[1.0, 5.0], bounds=([0, 0.1], [10, 100]))
    a,ksi=a_ksi
    
    return ksi


#main code, we are ready use our functions
def main_function(L,sample_step):
    Ts = np.linspace(0.2,5.0, 25)
    #do this at different Ts or equivalently Js
    T_energies=[]
    T_magnetism=[]
    T_Cv=[]
    T_chi=[]
    T_correlations=[]
    for T in Ts:
        energies=[]
        magnetism=[]
        #correlations=[]
        lattice=Lattice(L)
        for _ in range(100):
            lattice = metropolis(lattice, L, T)
            
        for sample in range(sample_step):
            lattice= metropolis(lattice,L,T)
        T_correlations.append(correlation(lattice,L))
    
    
        
    return Ts, T_correlations
    
Ts,T_correlations=main_function(50,30000)

''''T=[]
T_energies=[]
T_magnetism=[]
T_Cv=[]
T_chi=[]

for i in range(100):
    T1, T_energies1, T_magnetism1, T_Cv1,T_chi1=main_function(10,50,30)
    T.append(T1)
    T_energies.append(T_energies1)
    T_magnetism.append(T_magnetism1)
    T_Cv.append(T_Cv1)
    T_chi.append(T_chi1)
    
T=np.mean(T,axis=0)
T_energies=np.mean(T_energies,axis=0)
T_magnetism=np.mean(T_magnetism,axis=0)
T_Cv=np.mean(T_Cv,axis=0)
T_chi=np.mean(T_chi,axis=0)'''

    
    
plt.scatter(Ts,T_correlations,label='data')
plt.xlabel("Ts")
plt.ylabel("correlation")
plt.legend()
plt.show()
