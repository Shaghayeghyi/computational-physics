import numpy as np
import matplotlib.pyplot as plt
import math as m

#alright we need to create a triangle
#we need three coordinate in a 2D world
p1=np.array([0,0])
p2=np.array([1,0])
#the apex of equilateral Triangle
p3=np.array([1/2,m.sqrt(3)/2])
#get the set of coordinates to describe the T
tr=np.array([p1,p3,p2,p1])
'''plt.plot(tr[:,0], tr[:,1])
plt.show()'''
#i believe everything is very similar to the last code
#i need to work with three lines and i also need to work with three functions
#f1 should scale all 3 lines by 1/2
#f2 should do the same but transfer the new tri by (0, 1/2)
#f3 should scale too but it has a transfer by (1/4, sqrt3/4)
#another thing is thati nee a colored triangle to start with

def scale(l0):
    #scale by half
    S=np.array([[1/2,0],[0,1/2]])
    pi_new=np.dot(S,l0[0])
    pf_new=np.dot(S,l0[1])
    l1=np.array([pi_new,pf_new])
    return l0

def Transfer(l1):
    #scaling
    S=np.array([[1/2,0],[0,1/2]])
    #one direction transfer
    T=np.array([1/2,0])
    pi_new=np.dot(S,l1[0])+T
    pf_new=np.dot(S,l1[1])+T
    l1=np.array([pi_new,pf_new])
    return l1
def Transfer2(l2):
    #scaling
    S=np.array([[1/2,0],[0,1/2]])
    #one direction transfer
    T=np.array([1/4,m.sqrt(3)/4])
    pi_new=np.dot(S,l1[0])+T
    pf_new=np.dot(S,l1[1])+T
    l2=np.array([pi_new,pf_new])
    return l2




