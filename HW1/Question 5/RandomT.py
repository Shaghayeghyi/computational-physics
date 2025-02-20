import random
import matplotlib.pyplot as plt
import numpy as np

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
    return 1/2 +T
def Transfer2(1):
    #scaling
    #one direction transfer
    T2=np.array([1/4,m.sqrt(3)/4])
    return l/2+T2
#l is a pair (x,y)

