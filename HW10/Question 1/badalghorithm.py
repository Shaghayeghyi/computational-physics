#we want to see deviation from the real answer by using a bad algorithm
import numpy as np
import matplotlib.pyplot as plt


def bad(h,q0):
    steps = int(5/ h)
    time = np.zeros(steps + 1)
    qs=[]
    qs.append(q0)
    q1=q0+h*(1-q0)
    time[0]=0
    time[1]=h
    #or
    #q1=1-np.exp(-h)
    qs.append(q1)
    for step in range(1,steps):
        q_new=qs[step-1]+2*(1-qs[step])*h
        time[step+1]=time[step]+h
        qs.append(q_new)
        
    return time, qs



#define the real answer
def real_result(time_array):
    qs = 1 - np.exp(-time_array)
    return time_array, qs
    
#initial value
q0 = 0
T1, Q1 = bad(0.1,q0)
T2, Q2 = bad(0.08,q0)

T_real, Q_real = real_result(T1)

plt.figure(figsize=(10, 5))
plt.plot(T1, Q1, label=f"bad! h=0.1", color="purple", linewidth=1)
plt.plot(T2, Q2, label=f"bad! h=0.08", color="yellow", linewidth=1)
plt.plot(T_real, Q_real, label="exact", linewidth=2)
plt.xlabel("T")
plt.ylabel("Q")
#plt.title(f"bad vs Exact for h={h}")
plt.legend()
plt.grid(True)
plt.show()
