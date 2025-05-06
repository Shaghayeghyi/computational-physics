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
plt.plot(T, Q, label="Euler", linestyle="--")
plt.plot(T_real, Q_real, label="Exact", linewidth=2)
plt.xlabel("Time")
plt.ylabel("Q(t)")
plt.title(f"Euler vs Exact for h={h}")
plt.legend()
plt.grid(True)
plt.show()
