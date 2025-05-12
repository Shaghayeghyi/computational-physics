#we want to see deviation from the real answer by using a bad algorithm
import numpy as np
import matplotlib.pyplot as plt


def bad(h,q0):
    steps = int(5 / h)
    time = np.zeros(steps + 1)
    qs=[]
    qs.append(q0)
    q1=q0+h*(1-q0)
    time[0]=0
    #or
    #q1=1-np.exp(-h)
    qs.append(q1)
    for step in range(1,steps):
        q_new=qs[step-1]+2*(1-qs[step])*h
        time[step]=time[step-1]+h
        qs.append(q_new)
        
    return time, qs



#define the real answer
def real_result(time_array):
    qs = 1 - np.exp(-time_array)
    return time_array, qs
    
#initial value
h = 1e-1
q0 = 0
T, Q = bad(h,q0)

plt.plot(T,Q)
plt.show()
    
