import numpy as np
import matplotlib.pyplot as plt
import math as m
import random

#for fern fractal, we will need four transformation which are selfaffine
#these 4 functions should be applied with a non uniform prbability
#the functions responsible for the leaf structure should be applied more often for instance
#the process is the same as before and we need (x,y)
#four funtions
def f1(p):
    #define a the typical rotation matrix for a 2D space :)
    Ro=(np.array([[0.85, 0.04],[-0.04,0.85]]))
    T=np.array([0,1.6])
    p_new=np.dot(Ro,p)+T
    return p_new
def f2(p):
    #define a the typical rotation matrix for a 2D space :)
    Ro=(np.array([[0.2, -.26],[0.23,0.22]]))
    T=np.array([0,1.6])
    p_new=np.dot(Ro,p)+T
    return p_new
def f3(p):
    #define a the typical rotation matrix for a 2D space :)
    Ro=(np.array([[0, 0],[0,.16]]))
    T2=np.array([0,0])
    p_new=np.dot(Ro,p)+T2
    return p_new
def f4(p):
    Ro=(np.array([[-.15, 0.28],[0.26,0.24]]))
    T2=np.array([0,0.44])
    p_new=np.dot(Ro,p)+T2
    return p_new
#l is a pair (x,y)
N_points=100000
N_functions=50
function=[f1,f2,f3,f4]
#non uniform choosing method for functions
Probability=[0.85,0.07,0.01,0.07]
#we also have to save all of our generated final points
plotting_data=[]
for i in range(N_points):
    #numbers between 0 and 1
    pair0=np.array([random.random(),random.random()])
    #applying function
    for j in range(N_functions):
        #randomly chosen function
        f=np.random.choice(function, p=Probability)
        new_pair=f(pair0)
        #now for the next j loop we work with new_pair
        pair0=new_pair
    #after applying enough functions we need to save this final point
    plotting_data.append(pair0)
plotting_data=np.array(plotting_data)
plt.figure(figsize=(8, 8))
plt.scatter(plotting_data[:, 0], plotting_data[:, 1],s=0.1,color='blue')
plt.savefig("100000.jpg")
plt.show()

