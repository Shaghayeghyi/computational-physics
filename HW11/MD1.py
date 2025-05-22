import numpy as np
import matplotlib.pyplot as plt

#initial values
@jit(nopython=True)
def initial():
    #3.4×10 −10 m
    sigma=1
    #6.63×10^−26kg
    m=1
    #1.65×10 −21 J
    epsilon=1
    L=20
    N=100
    V_max=1.5
    #initial configuration
    X=np.zeros((N,2))
    V=np.zeros((N,2))
    n_site= int(np.ceil(np.sqrt(N)))
    # Place in left half of box (L/2 x L)
    box_x = L / 2
    spacing = box_x / n_side
    count = 0
    for i in range(n_site):
        for j in range(n_site):
            if count >= N:
                break
            X[count, 0] = i * spacing + spacing / 2 
            X[count, 1] = j * spacing + spacing / 2
            count += 1
        if count >= N:
            break
            
    for i in range(N):
        for j in range(2):
            velocities[i, j] = np.random.uniform(-V_max, V_max)

    #now we need the CM coordinate
    


    
    
    
    
    
    
