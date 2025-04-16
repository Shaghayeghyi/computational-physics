#gaussian integral with metropolis algorithm
import numpy as np
import matplotlib.pyplot as plt
import random

#assume the equilibrium
def Gaussian_p(x):

    g=np.exp(-(x)**2)
    return g


def metropolic(size,step):
    #rate of condition's acceptance
    accept_count=0
    x=0
    number_array=[]

    for loop in range(size):
        #move
        y=x+step*np.random.uniform(-1,1)
        px=Gaussian_p(x)
        py=Gaussian_p(y)

        if np.random.uniform(0,1)<(py/px):
            x=y
            accept_count+=1
    
        number_array.append(x)

    rate=accept_count/size
    return rate, number_array

            
#print(metropolic(1000,0.1))


step=0.35
rate, array=metropolic(1000000,step)
print(f"this is the rate of acceptance:{rate} for step={step}")
'''plt.hist(array, bins=70, alpha=0.7,rwidth=0.85, density=True)
plt.title(f"gaussian histogram for step={step}")
plt.show()'''

#for various js from 0 to 100
def correlation(array):
    n=len(array)
    sigma=np.var(array)
    correlation_js=[]
    for j in range(100):
        sum_ij=0
        sum_j=0
        for i in range(n-j):
            sum_ij+=array[i]*array[i+j]
            sum_j+=array[i+j]
        mean_ij=sum_ij/(n-j)
        mean_j=sum_j/(n-j)
        lenght_j=(mean_ij-np.mean(array)*mean_j)/sigma
        correlation_js.append(lenght_j)

    return correlation_js
            
print(correlation(array))        




    

        

        

    
    



     


