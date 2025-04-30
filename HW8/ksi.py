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





#new version
def correlation_length(lattice, L, threshold=0.2):
    meanL = np.mean(lattice)
    varianceL = np.var(lattice)
    
    #very uniform lattice
    if varianceL < 1e-6:
        return 0.0
    
    max_shift = min(L//2, 20)
    
    # Check both x and y directions and then average it
    shifts = []
    corrs = []
    for shift in range(1, max_shift + 1):
       
        shifted_x = np.roll(lattice, shift, axis=1)
        corr_x = np.mean(lattice * shifted_x) - meanL**2
        
      
        shifted_y = np.roll(lattice, shift, axis=0)
        corr_y = np.mean(lattice * shifted_y) - meanL**2
        
        
        corr = (corr_x + corr_y)/2
        normalized_corr = corr / varianceL
        
        shifts.append(shift)
        corrs.append(normalized_corr)
        
        #stop if correlation becomes too small
        if abs(normalized_corr) < threshold:
            break
    
    if len(shifts) < 2:
        return 0.0
    

    log_corrs = np.log(np.maximum(corrs, 1e-10))  #protect against log(0)
    slope, _ = np.polyfit(shifts, log_corrs, 1)
    
    if slope >= -1e-6:  
        return 0.0
    
    return -1/slope






def correlation(lattice,L,T):
    mean_spin = np.mean(lattice)
    var_spin = np.var(lattice)
    
    if var_spin<10**-6:
        return 0.2
        
    max_shift = int(L/2)
    '''if T < 1.5:
        max_shift = min(int(L/2), 50)  #longer range
    elif T > 3.0:
        max_shift = min(int(L/4), 10)  # shorter range is cool :)
    else:  #this is around Tc
        max_shift = int(L/3)'''
    mean_products = []
    
    for shift in range(max_shift):
        rolled_x = np.roll(lattice, shift, axis=1)
        rolled_y = np.roll(lattice, shift, axis=0)
        Cx = np.mean(rolled_x * lattice) - mean_spin**2
        Cy = np.mean(rolled_y * lattice) - mean_spin**2
        mean_products.append((Cx + Cy)/(2 * var_spin))
    
    C_shift = np.array(mean_products)
    

    fit_length = min(10, max_shift)
    shifts = np.arange(fit_length)
    
    def exp_decay(shift, ksi):
        return np.exp(-shift / ksi)

    try:
        ksi_opt, _ = curve_fit(exp_decay, shifts, C_shift, p0=[1.0], bounds=([0.01], [100]))
        if T<0.5:
            if ksi_opt[0]>2:
                return np.nan
        else:
            return ksi_opt[0]
        
    except:
        return np.nan

def maxs(array,Ts,name,L):
    max_index = np.nanargmax(array)
    Tc_L = Ts[max_index]
    print(f"Estimated Tc of {name} for L={L}: {Tc_L}")
    val_Tc = array[max_index]
    print(f"Estimated value of {name}(Tc) = {val_Tc:}")
    return

#main code, we are ready use our functions
def main_function(L,sample_step):
    Ts = np.linspace(0.8, 7, 30)
    '''Ts = np.concatenate([
    np.linspace(0.8, 1.8, 5),
    np.linspace(2.0, 2.6, 30),
    np.linspace(3.0, 7.0, 5)])'''
    #do this at different Ts or equivalently Js
    T_energies=[]
    T_magnetism=[]
    T_Cv=[]
    T_chi=[]
    T_correlations=[]
    lattice=Lattice(L)
    for T in Ts:
        energies=[]
        magnetism=[]
        #correlations=[]
        for _ in range(500):
            lattice = metropolis(lattice, L, T)
        cors=[]
        for sample in range(sample_step):
            lattice= metropolis(lattice,L,T)
            if sample%10==0: #every 10 steps in phase space
                 cors.append(correlation_length(lattice, L))
        T_correlations.append(np.mean(cors) if cors else np.nan)
    maxs(T_correlations, Ts, "ksi", L)
    
        
    return Ts, T_correlations
Ls=[8,16,32,64]
x=10000
for L in Ls:
    Ts,T_correlations=main_function(L,x)   
    plt.scatter(Ts,T_correlations,label=f'L={L}')
    #plt.title(f"this is for L={L}")
    plt.xlabel("Ts")
    plt.ylabel("correlation")
    plt.legend()
plt.show()


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
