#gaussian integral with metropolis algorithm
import numpy as np
import matplotlib.pyplot as plt
import random

#assume the equilibrium
def Gaussian_p(x,mean,sigma):

    g=(1/np.sqrt(2*np.pi*sigma))*np.exp(-(x-mean)**2/(2*sigma**2))
    return g


def metropolic(size,step):
    



     


