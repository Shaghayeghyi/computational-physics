import random
import matplotlib.pyplot as plt
import numpy as np
import math as m

#we will create a random number. for creating the triangle we will randomly choose between f1 f1 and f3 and apply it on the point
#we will then apply the chosen f on our P and use the new point and repeat the algorithm.
#we use tons of random points for this and plot everything at last

#three funtions
def scale(l):
    #scale by half
    return l/2
def Transfer(l):
    #scaling
    #one direction transfer
    T=np.array([1/2,0])
    return l/2 +T
def Transfer2(l):
    #scaling
    #one direction transfer
    T2=np.array([1/4,m.sqrt(3)/4])
    return l/2+T2
#l is a pair (x,y)
N_points=10000
N_functions=50
function=[scale,Transfer,Transfer2]
#we also have to save all of our generated final points
plotting_data=[]
for i in range(N_points):
    #numbers between 0 and 1
    pair0=np.array([random.random(),random.random()])
    #applying function
    for j in range(N_functions):
        #randomly chosen function
        f=random.choice(function)
        new_pair=f(pair0)
        #now for the next j loop we work with new_pair
        pair0=new_pair
    #after applying enough functions we need to save this final point
    plotting_data.append(pair0)
plotting_data=np.array(plotting_data)
plt.figure(figsize=(8, 8))
plt.scatter(plotting_data[:, 0], plotting_data[:, 1],s=0.1,color='blue')
plt.show()
