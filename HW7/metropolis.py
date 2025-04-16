#gaussian integral with metropolis algorithm
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.optimize import curve_fit

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

'''def Gaussian_p_N(x):

    g=1/np.sqrt(2*np.pi)*np.exp(-(x)**2)
    return g           
#print(metropolic(1000,0.1))
xs= np.linspace(-5, 5, 500)
y = Gaussian_p_N(xs)'''

step=11
rate, array=metropolic(1000000,step)
print(f"this is the rate of acceptance:{rate} for step={step}")
plt.hist(array, bins=70, alpha=0.7,rwidth=0.85, density=True)
plt.plot(xs,y)
plt.title(f"gaussian histogram for step={step}")
plt.show()

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
            
Cor=correlation(array)
#ksi=len(np.array(Cor)[np.array(Cor)>np.exp(-1)])
#print(f"this is ksi{ksi}")

threshold = 1/np.e
for j, value in enumerate(Cor):
    if value < threshold:
        print(f"Correlation length is j = {j} (value = {value:})")
        break

def exp_decay(j, a, ksi):
    return a * np.exp(-j /ksi)
    
J=np.arange(100)
a_ksi, cov=curve_fit(exp_decay, J, Cor,p0=[1, 10])
a,ksi=a_ksi
print(f"this is ksi by fit={ksi}")
plt.scatter(J,Cor,label='data')
plt.plot(J,a * np.exp(-J /ksi),label='fit')
plt.xlabel("Js")
plt.ylabel("correlation")
plt.legend()
plt.show()





    

        

        

    
    



     


