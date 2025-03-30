#for this question i will create my own string of numbers using module
import numpy as np
import matplotlib.pyplot as plt
import time
#use time
x = int(time.time())
def module(x,a,c,m):
    return (a*x+c)%m

def generator1(N):
    #define the parameters
    m=2**31
    c=1013904223
    a=1664525
    module_array=[]
    for num in range(N):
        x=module(x,a,c,m)
        #between 0 and 9
        module_array.append(x%10)
        
    return module_array

N=100000
#print(generator(100))
x_axis=np.arange(10)
plt.title(f"distribution for {N} loops")
plt.ylabel("distribution") 
plt.xlabel("numbers")
plt.bar(x_axis,generator1(N))           
plt.show()
#log log plot for sigma
#one run
runs=1
Ns=np.logspace(2, 5, num=20).astype(int)
all_N=[]
for N in Ns:
    means=[]
    for run in range(runs):
        means.append(generator1(N))
    mean=np.mean(means, axis=0)
    all_N.append(np.std(mean)/N)
    
logN=np.log(Ns)
logSigma=np.log(all_N)
plt.scatter(logN,logSigma)
plt.ylabel("log sigma/sqrtN") 
plt.xlabel("log N")
a,b = np.polyfit(logN, logSigma, deg =1)
fit=a*logN+b
plt.plot(logN, fit, label=f"slope is {a}")
plt.legend()
plt.show()   
          
