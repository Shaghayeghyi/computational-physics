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


#define other sols
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
    

h=0.01
T_real, V_real, X_real = real_sol(h)
T_euler, V_euler, X_euler = euler(h)
T_cromer, V_cromer, X_cromer =  euler_cromer(h)


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(T_real, X_real, label='exact', linestyle='--')
plt.plot(T_euler, X_euler, label='euler', alpha=0.7)
plt.plot(T_cromer, X_cromer, label='cromer', alpha=0.7)
plt.xlabel("T")
plt.ylabel("X")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(X_real, V_real, label='exact', linestyle='--')
plt.plot(X_euler, V_euler, label='euler', alpha=0.7)
plt.plot(X_cromer, V_cromer, label='cromer', alpha=0.7)
plt.xlabel("X")
plt.ylabel("V")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
