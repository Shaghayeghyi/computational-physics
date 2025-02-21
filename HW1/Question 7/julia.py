import numpy as np
import matplotlib.pyplot as plt
import random
import math as m

#for the julia set we need to work with complex numbers
#we have a boundary with lenght r. we choose a random number
#we apply a function f(z) on it till it either gets out of boundary or we just reach the max iteration
#we save the number of iteration done for each random number and assigne a color to each

#i want to create a random number between 0 and 10


'''x=random.uniform(0,10)
y=random.uniform(0,10)
z=complex(x,y)
print(Ncomplex)'''
#boundary distance
r=5

N_iteration=[]
#how many random numbers
N_randoms=1000
#Max iteration number of function
Max=20

def z_function(z):
    c=complex(0,0.1)
    f=z**2+c
    return f
#data is an array saving the final z and the number of iterations
data=[]
#for all random numbers
for i in range(N_randoms):
    x=random.uniform(0,10)
    y=random.uniform(0,10)
    z=complex(x,y)
    #counter
    l=0
    #for all iterations
    for j in range(Max):
        if abs(z)<=r and j<=Max:
            z=z_function(z)
            l=l+1
        point=np.array([z,l])
        data.append(point)
        #get back to the next number
        continue
    
