import numpy as np
import matplotlib.pyplot as plt
from time import time


def euler(h,q,step):
    time=np.zeros(step+1)
    qs=[]
    qs.append(q)
    for i in range(step):
        q=q+h*(1-q)
        qs.append(q)
        time[i+1]=time[i]+h

    return time , qs

# Parameters
h = 10**-4
q0 = 0
steps = int(5 / h)

T,Q=euler(h,q0,steps)        


#define the real answer
def real_result(time_array):
    qs = 1 - np.exp(-time_array)
    return time_array, qs
    

T_real, Q_real =real_result(T)

plt.figure(figsize=(10, 5))
plt.scatter(T, Q, s=1 , color="red", label="Euler")
plt.plot(T_real, Q_real, label="Exact", linewidth=2)
plt.xlabel("Time")
plt.ylabel("Q(t)")
plt.title(f"Euler vs Exact for h={h}")
plt.legend()
plt.grid(True)
plt.show()



hs=np.logspace(-6 , -1 , 100)

errors = []

for h in hs:
    q0=0
    steps = int(5 / h)
    T, Q = euler(h, q0,steps)
    T_real, Q_real = real_result(T)
    #relative error at the final step
    err = abs(Q[-1] - Q_real[-1]) / Q_real[-1]
    errors.append(err)


plt.figure(figsize=(8, 5))
plt.plot(np.log(hs), np.log(errors), marker='o', linestyle='-', color='blue')
plt.xlabel("h")
plt.ylabel("relative error")
a,b =np.polyfit(np.log(hs),np.log(errors),1)
print(f"the slope of the fit is{a}")
#plt.plot(hs, a*hs+b ,label=f'the slop is {a}')
plt.grid(True)
plt.show()
