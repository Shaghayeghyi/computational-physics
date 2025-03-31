import numpy as np
import matplotlib.pyplot as plt
from random import randint,random

def gaussian():
    #we will first have two uniform variables
    x1=np.random.rand()
    x2=np.random.rand()
    #we have transformation to rho and theta 
    rho=sigma*np.sqrt(-2*np.log(1-x1))
    theta=2*np.pi*x2
    #now have y1 and y2
    y1=rho*np.cos(theta)
    y2=rho*np.sin(theta)
