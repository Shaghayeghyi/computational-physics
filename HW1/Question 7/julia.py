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
'''#boundary distance
r=2

N_iteration=[]
#how many random numbers
N_randoms=50000
#Max iteration number of function
Max=50

def z_function(z):
    c=complex(-0.4,-0.6)
    f=z**2+c
    return f
#data is an array saving the final z and the number of iterations
data=[]
#for all random numbers
for i in range(N_randoms):
    #to cover the whole parts of page
    x=random.uniform(-3,3)
    y=random.uniform(-3,3)
    z=complex(x,y)
    #counter
    l=0
    #for all iterations
    while abs(z)<=r and l<=Max:
        z=z_function(z)
        l=l+1
    point=np.array([x,y,l])
    data.append(point)
data=np.array(data)
#just checking
print(data[:,1])

colors = plt.cm.viridis(np.linspace(0, 1, Max))
print(colors)
plt.figure(figsize=(8, 8))
plt.scatter(data[:, 0], data[:, 1], c=data[:, 2], cmap='plasma',s=0.5)
plt.show()'''


N_randoms=50000
#Max iteration number of function
Max=50

#for creating a better plot maybe i should work with the pixels instead of points.
#i will have a plane in this limit (xi,xf) and (yi,yf)
xi,xf=-10,10
yi,yf=-10,10
r=2
#each number is a pixel in my mind so at first i will create a 2D array 20x20
initial_value=np.zeros((20,20))
def z_function(z):
    c=complex(-0.4,-0.6)
    f=z**2+c
    return f
#now i will create random numbers in this plane and assign a new number l instead of zero to each pixel

for i in range(N_randoms):
    #to cover the whole parts of page
    x=random.uniform(-10,10)
    y=random.uniform(-10,10)
    z=complex(x,y)
    #counter
    l=0
    #for all iterations
    while abs(z)<=r and l<=Max:
        z=z_function(z)
        l=l+1
    initial_value[x,y]=l



