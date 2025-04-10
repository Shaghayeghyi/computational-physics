import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import random

#with a basic analogy with the pool example, we will calculate the given integral


def real_result():

    def f_x(x):
        return -x**3 + 5*x
    
    answer , error = quad(f_x, 0, 2)

    return answer

#what is the real output
result=real_result()


#approximation of min and max of function for correct boundary

def min_max():
    x_vals = np.linspace(0, 2, 1000)  # 1000 points in [0, 2]
    y_vals = -x_vals**3 + 5*x_vals

    return np.min(y_vals) , np.max(y_vals)



def shelep(N):
    Np=0
    min_y , max_y= min_max()
    for i in range(N):
        random_y=np.random.uniform(min_y, max_y+5)
        random_x=np.random.uniform(0,2)
        F=-random_x**3+5*random_x
        if random_y<F:
            Np+=1

    return 2*(max_y+5)*Np/N
    

print(f"this is the result of shelep for N=100000:{shelep(100000)}")

#let's plot the difference

Ns = np.arange(1000, 100000, 2000, dtype=int)

difference=[]
#we can get mean of runs
runs=10
mean_diff=[]
for N in Ns:
    for run in range(runs):
        diff=np.abs(real_result()-shelep(N))
        mean_diff.append(diff)
    difference.append(np.mean(mean_diff))
plt.plot(Ns,difference)
plt.xlabel("N")
plt.ylabel("difference")
plt.show()
    
        
     

     
     
