import numpy as np
import matplotlib.pyplot as plt



def euler(h):
    #i want the time be the same for all of my functions
    #omega=1
    time = np.arange(0, 60, h)
    l=len(time)
    xs = [1]
    vs = [0]
    for n in range(l - 1):
        x_new = xs[n] + h * vs[n]
        v_new = vs[n] - h * xs[n]
        xs.append(x_new)
        vs.append(v_new)

    return time, np.array(vs), np.array(xs)


def real_sol(h):
    #i want the time be the same for all of my functions
    #omega=1
    time = np.arange(0, 60, h)
    xs = np.cos(time)
    vs = -np.sin(time)
    return time, vs, xs


#other solution with cromer
def euler_cromer(h):
    #i want the time be the same for all of my functions
    #omega=1
    time = np.arange(0, 60, h)
    l=len(time)
    xs = [1]
    vs = [0]
    for n in range(l - 1):
        v_new = vs[n] - h * xs[n]
        vs.append(v_new)
        x_new = xs[n] + h * vs[n+1]
        xs.append(x_new)
        

    return time, np.array(vs), np.array(xs)

#leap frog
def leap(h):
    #a=-1
    time = np.arange(0, 60, h)
    xs = [1]
    #vs_full=[0]
    #we need to use euler for the first step as explained
    vs_half=[0.5*h*1]
    
    for n in range(len(time) - 1):
        #v_full_new=vs_full[n]-xs[n]*h
        #vs_full.append(v_full_new)
        vs_half_new = vs_half[n]-xs[n]* h
        vs_half.append(vs_half_new)
        x_new = xs[n] + vs_half[n + 1] * h
        xs.append(x_new)
    #an average
    vs_full = []
    for i in range(1,len(time)):
        v_full = (vs_half[i-1] + vs_half[i]) / 2
        vs_full.append(v_full)
    vs_full.append(vs_half[-1] - 0.5 * h * xs[-1])
    
        
    return time, np.array(vs_full), np.array(xs)


def verlet(h):
    # a = -x 
    time = np.arange(0, 60, h)
    xs = [1] 
    vs = [0] 
    #again i need to use euler for derving another value
    x1 = xs[0] + h * vs[0]
    xs.append(x1)
    v1=(xs[1]-xs[0])/(2*h)
    vs.append(v1)
    for n in range(1, len(time)-1):
        x_new = 2*xs[n]-xs[n-1] -xs[n]*h*h
        xs.append(x_new)
        v_new = (xs[n+1] - xs[n-1]) / (2 * h)
        vs.append(v_new)
    
    return time, np.array(vs), np.array(xs)


def Vverlet(h):
    # a = -x 
    time = np.arange(0, 60, h)
    xs = [1] 
    vs = [0] 
    
    for n in range(len(time)-1):
        x_new = xs[n]+h*vs[n] -0.5*xs[n]*h*h
        xs.append(x_new)
        v_new = vs[n]-0.5*h*(xs[n]+xs[n+1])
        vs.append(v_new)
    
    return time, np.array(vs), np.array(xs)


    
h=0.01
T_real, V_real, X_real = real_sol(h)
T_euler, V_euler, X_euler = euler(h)
T_cromer, V_cromer, X_cromer =  euler_cromer(h)
T_leap, V_leap, X_leap = leap(h)
T_verlet, V_verlet, X_verlet = verlet(h)
T_Vverlet, V_Vverlet, X_Vverlet = Vverlet(h)


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(T_real, X_real, label='exact', linestyle='--')
plt.plot(T_euler, X_euler, label='euler', alpha=0.7)
plt.plot(T_cromer, X_cromer, label='cromer', alpha=0.7)
plt.plot(T_leap, X_leap, label='leap', alpha=0.7)
plt.plot(T_verlet, X_verlet, label='verlet', alpha=0.7)
plt.plot(T_Vverlet, X_Vverlet, label='Vverlet', alpha=0.7)
plt.xlabel("T")
plt.ylabel("X")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(X_real, V_real, label='exact', linestyle='--')
plt.plot(X_euler, V_euler, label='euler', alpha=0.7)
plt.plot(X_cromer, V_cromer, label='cromer', alpha=0.7)
plt.plot(X_leap, V_leap, label='leap', alpha=0.7)
plt.plot(X_verlet, V_verlet, label='verlet', alpha=0.7)
plt.plot(X_Vverlet, V_Vverlet, label='Vverlet', alpha=0.7)
plt.xlabel("X")
plt.ylabel("V")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
