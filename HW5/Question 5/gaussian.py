import numpy as np
import matplotlib.pyplot as plt
from random import randint,random

def gaussian(runs ,sigma=1):
    #runs=10000
    y1s=[]
    y2s=[]
    for run in range(runs):
        #we will first have two uniform variables
        x1=np.random.rand()
        x2=np.random.rand()
        #we have transformation to rho and theta 
        rho=sigma*np.sqrt(-2*np.log(1-x1))
        theta=2*np.pi*x2
        #now have y1 and y2
        y1=rho*np.cos(theta)
        y2=rho*np.sin(theta)
        y1s.append(y1)
        y2s.append(y2)
    return y1s , y2s

Y1s , Y2s=gaussian(100000)
plt.hist(Y1s, bins=50 ,alpha=0.7, rwidth=0.85 , density=True , label="from rho")
plt.hist(Y2s, bins=50 ,alpha=0.7, rwidth=0.85 , density=True , label="from theta")
plt.xlabel("y1 and y2")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
