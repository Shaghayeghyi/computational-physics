import numpy as np
import matplotlib.pyplot as plt
import random


def grid():
    N=60
    #ratio of empty and 1 and 2
    ratio1=0.4
    ratio2=0.4
    ratio0=0.2
    Bm=0.75
    values = [0, 1, 2]
    weights = [ratio0, ratio1, ratio2] 
    # Create grid
    grid = np.random.choice(values, size=(N,N), p=weights)
    return grid
        
g = grid()
plt.imshow(g, cmap='coolwarm')
plt.title("Randomly Created Grid")
plt.show()
