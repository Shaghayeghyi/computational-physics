import numpy as np
import matplotlib.pyplot as plt
import math as m
import random

#for fern fractal, we will need four transformation which are selfaffine
#these 4 functions should be applied with a non uniform prbability
#the functions responsible for the leaf structure should be applied more often for instance
#the process is the same as before and we need (x,y)
#four funtions
def f1(l0):
    #define a the typical rotation matrix for a 2D space :)
    Ro=(np.array([[0.85, 0.4],[0.3,0]]))
    pi_new=np.dot(Ro,l0[0])
    pf_new=np.dot(Ro,l0[1])
    #new line
    l1=np.array([pi_new,pf_new])
    T=np.array([1/2,0])
    return l1+T
def f2(l0):
    #define a the typical rotation matrix for a 2D space :)
    Ro=(np.array([[0.3, 0.4],[0.3,0.4]]))
    pi_new=np.dot(Ro,l0[0])
    pf_new=np.dot(Ro,l0[1])
    #new line
    l1=np.array([pi_new,pf_new])
    T=np.array([1/2,0])
    return l1+T
def f3(l0):
    #define a the typical rotation matrix for a 2D space :)
    Ro=(np.array([[0.3, 0.4],[0.3,0.4]]))
    pi_new=np.dot(Ro,l0[0])
    pf_new=np.dot(Ro,l0[1])
    #new line
    l1=np.array([pi_new,pf_new])
    T2=np.array([1/4,m.sqrt(3)/4])
    return l1++T2
def f4(l0):
    Ro=(np.array([[0, 0.45],[0.3,0.4]]))
    pi_new=np.dot(Ro,l0[0])
    pf_new=np.dot(Ro,l0[1])
    #new line
    l1=np.array([pi_new,pf_new])
    T2=np.array([1/4,m.sqrt(3)/4])
    return l1+T2
#l is a pair (x,y)
N_points=10000
N_functions=50
function=[f1,f2,f3,f4]
#non uniform choosing method for functions
Probability=[0.85,0.10,0.02,0.03]
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
plt.show()
def R_45(l0):
    #45 degree rotation and scaling combined
    tetha=45
    degree=np.radians(tetha)
    #define a the typical rotation matrix for a 2D space :)
    Ro=(np.array([[np.cos(degree), -np.sin(degree)],[np.sin(degree),  np.cos(degree)]]))*1/m.sqrt(2)
    pi_new=np.dot(Ro,l0[0])
    pf_new=np.dot(Ro,l0[1])
    #new line
    l1=np.array([pi_new,pf_new])
    return l1
