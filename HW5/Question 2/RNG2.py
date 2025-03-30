import numpy as np
import matplotlib.pyplot as plt
from random import randint,random

#let's look at python's RNG

def generator(N):
    
    number_array=np.zeros(10)
    string=[]
    for num in range(N):
        random_number = randint(0,9)
        string.append(random_number)
    
    for number in range(len(string)):

        if string[number]==4 and number!=len(string)-1:
            focus=string[number+1]
            number_array[focus]+=1
            
    
        

    return number_array
N=110000
#print(generator(100))
x_axis=np.arange(10)
plt.title(f"distribution with correlation for {N} loops")
plt.ylabel("distribution") 
plt.xlabel("numbers")
plt.bar(x_axis,generator(N))           
plt.show()
#log log plot for sigma
#one run
runs=1
Ns=np.logspace(2, 5, num=20).astype(int)
all_N=[]
for N in Ns:
    means=[]
    for run in range(runs):
        means.append(generator(N))
    mean=np.mean(means, axis=0)
    all_N.append(np.std(mean)/N)
    
logN=np.log(Ns)
logSigma=np.log(all_N)
plt.scatter(logN,logSigma)
plt.ylabel("log sigma/N") 
plt.xlabel("log N")
a,b = np.polyfit(logN, logSigma, deg =1)
fit=a*logN+b
plt.plot(logN, fit, label=f"slope is {a}")
plt.legend()
plt.show() 
    
