import numpy as np
import matplotlib.pyplot as plt
import random

Bm=0.75

def grid():
    N=60
    #ratio of empty and 1 and 2
    ratio1=0.4
    ratio2=0.4
    ratio0=0.2
    values = [0, 1, 2]
    weights = [ratio0, ratio1, ratio2] 
    # Create grid
    grid = np.random.choice(values, size=(N,N), p=weights)
    return grid
        
g = grid()
'''plt.imshow(g, cmap='coolwarm')
plt.title("Randomly Created Grid")
plt.show()'''


def happiness(grid, i,j):
    N=grid.shape[0]
    agent=grid[i,j]
    moves=[1,0,-1]
    #check all possible moore neighbors
    same=0
    diff=0
    for l in [-1, 0, 1]:
        for m in [-1, 0, 1]:
            # skip self
            if l == 0 and m == 0:
                continue 
            ni, nj = i + l, j + m
            if 0 <= ni < N and 0 <= nj < N:
                neighbor = grid[ni, nj]
                if neighbor != 0:
                    if neighbor == agent:
                        same += 1
                    else:
                        diff += 1

    total = same + diff
    if total == 0:
        return True
    #??
    return True if (same / (diff+same)) >= Bm


def find_unhappy(grid):
    unhappy=[]
    empty=[]
    N=grid.shape[0]
    for i in range(N):
        for j in range(N):
            if grid[i,j]==0:
                empty.append((i,j))
            elif not happiness(grid, i,j):
                unhappy.append((i,j))

    return empty, unhappy
                
            
            
            
            
    
