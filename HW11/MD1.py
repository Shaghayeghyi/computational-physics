import numpy as np
import matplotlib.pyplot as plt
from numba import njit

#initial values
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
    spacing =box_x / n_site
    count = 0
    for i in range(n_site):
        for j in range(n_site):
            if count >= N:
                break
                
            X[count, 0] = i * spacing + spacing / 2 
            X[count, 1] = j *2* spacing + spacing / 2
            count += 1
        
            
    for i in range(N):
        for j in range(2):
            V[i, j] = np.random.uniform(-V_max, V_max)

    #now we need the CM coordinate
    V_cm = np.mean(V, axis=0)
    V -= V_cm


    return X,V,L,N


X0,V0,L,N=initial()


'''plt.figure(figsize=(6, 6))
plt.scatter(X0[:, 0], X0[:, 1], s=20, color='blue', alpha=0.7)
plt.xlim(0, L)
plt.ylim(0, L)
plt.title("initial configuration")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()'''


def K_t(V_t):
    return 0.5*np.sum(V_t**2)


@njit
def U_t(X_t,L,N ,cut_off):
    cut_off2 = cut_off * cut_off
    U = 0.0
    #this method get's less time
    inv_rc2 = 1/ (cut_off2)
    inv_rc6 = inv_rc2 ** 3
    inv_rc12 = inv_rc6 ** 2
    V_shift = 4.0 * (inv_rc12 - inv_rc6)
    #at the end we will subtact this
    
    for i in range(N):
        xi, yi = X_t[i, 0], X_t[i, 1]
        for j in range(i + 1, N):
            dx = xi - X_t[j, 0]
            dy = yi - X_t[j, 1]
            #the real distance according to boundary condition
            dx -= L * round(dx / L)
            dy -= L * round(dy / L)

            rij2 = dx * dx + dy * dy
            #we have potential only inside the cut_off radius
            if rij2 < cut_off2:
                inv_r2 = 1.0 / rij2
                inv_r6 = inv_r2 ** 3
                inv_r12 = inv_r6 ** 2
                Uij = 4.0 * (inv_r12 - inv_r6) - V_shift
                U += Uij

    return U
    
    
    
    
    



    
    
    
    
    
    
