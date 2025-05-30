import numpy as np
import matplotlib.pyplot as plt
from numba import njit
import matplotlib.animation as animation
from scipy.stats import linregress

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
    
    
@njit
def F_t(X_t, L, N, cut_off):
    F = np.zeros((N, 2))
    cut_off2 = cut_off ** 2
    #we can calculate the virial of the system using these loops at once
    virial=0
    for i in range(N):
        xi, yi = X_t[i, 0], X_t[i, 1]
        for j in range(i + 1, N):
            dx = xi - X_t[j, 0]
            dy = yi - X_t[j, 1]

            dx -= L * round(dx / L)
            dy -= L * round(dy / L)

            rij2 = dx * dx + dy * dy

            if rij2 < cut_off2:
                inv_r2 = 1.0 / rij2
                inv_r6 = inv_r2 ** 3
                inv_r12 = inv_r6 ** 2
                force_scalar = 48 * inv_r2 * (inv_r12 - 0.5 * inv_r6)
                fx = force_scalar * dx
                fy = force_scalar * dy

                #newton's 3d law!
                F[i, 0] += fx
                F[i, 1] += fy
                F[j, 0] -= fx
                F[j, 1] -= fy
                virial+=(dx*fx+dy*fy)

    return F ,virial
    

@njit
def one_verlet_step(X0, V0, F0, L, N, h, cut_off):
   
    X_new= X0+ V0 * h + 0.5 * F0 * h**2
    for i in range(N):
        for d in range(2):
            X_new[i, d] = X_new[i, d] % L

    F_new,_ = F_t(X_new, L, N, cut_off)

    V_new = V0 + 0.5 * (F0 + F_new) * h

    return X_new, V_new, F_new


def MD():
    #now let's get eady for MD
    h=0.01
    T=10000
    cut_off=3
    saving=10
    warm_up=500
    #save the info of the whole system at each time step
    Xs=[]
    #initial
    X, V, L, N = initial()
    F , virial= F_t(X, L, N, cut_off)
    for step in range(warm_up):
        X, V, F = one_verlet_step(X, V, F, L, N, h, cut_off)
    for step in range(T):
        X, V, F = one_verlet_step(X, V, F, L, N, h, cut_off)
        Xs.append(X)
    
            

    return Xs
    
'''#a check for how the array works:
X=[[[1,4],[9,8],[10,12],[14,15]],[[7,21],[23,40],[71,80],[90,19]]]
X=np.array(X)
Xs=X[0]*X[1]
print(Xs)
Xss=np.sum(Xs,axis=1)
print(Xss)
'''

positions = MD()
positions = np.array(positions)
T, N, dim = positions.shape
h = 0.01 
L = 20 

#for each time
rms = np.zeros(T)
for t in range(T):
    delta_r = positions[t] - positions[0]
    #we need to take the real displacement into account for RMS
    delta_r = delta_r - L * np.round(delta_r / L)
    squared_d = np.sum(delta_r**2, axis=1)
    rms[t] =np.sqrt(np.mean(squared_d))

times = np.arange(T) * h


fit_range = slice(500, 1500)
log_times = np.log(times[fit_range])
log_rms = np.log(rms[fit_range])


a,b=np.polyfit(log_times,log_rms,1)
D = (np.exp(b) / 2)**2


plt.figure(figsize=(8, 5))
plt.plot(log_times, log_rms, 'b.', label='Log(RMS)')
plt.plot(log_times, b + a * log_times, 'r--', label="fit")
plt.xlabel('log(Time)')
plt.ylabel('log(RMS)')
plt.legend()
plt.grid(True)
plt.show()

print(f"Slope = {a:}")
print(f"Intercept = {b:}")
print(f"Diffusion constant D = {D:}")
