'''import numpy as np
import matplotlib.pyplot as plt
import random

Bm=0.75
def grid(ratio0):
    N=60
    ratio1=(1-ratio0)/2
    ratio2=(1-ratio0)/2
    #ratio of empty and 1 and 2
    values = [0, 1, 2]
    weights = [ratio0, ratio1, ratio2] 
    # Create grid
    grid = np.random.choice(values, size=(N,N), p=weights)
    return grid
        

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
    return (same / (diff+same)) >= Bm


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
                
            
def move_agents(grid, empty, unhappy):
    random.shuffle(empty)
    random.shuffle(unhappy)
    #we need random choices!
    for agent_pos, empty_pos in zip(unhappy, empty):
        ai, aj = agent_pos
        ei, ej = empty_pos
        grid[ei, ej] = grid[ai, aj]
        #leave empty behind
        grid[ai, aj] = 0  

    return grid          



def simulate(grid):
    max_steps=500
    history = [grid.copy()]
    moves=0
    for step in range(max_steps):
        empty, unhappy = find_unhappy(grid)
        if not unhappy:
            #print(f"Equilibrium reached at step {step}")
            break
        grid = move_agents(grid, empty, unhappy)
        history.append(grid.copy())
        moves+=1
    
    return history, moves


rhos=np.linspace(0.1, 1.0, 30)
moving=[]
for rho in rhos:
    g=grid(rho)
    means=[]
    for i in range(10):
            G=g.copy()
            _, moves=simulate(G)
            means.append(moves)
    moving.append(np.mean(means))
    

plt.plot(rhos, moving, marker='o', linestyle='-', color='b')
plt.xlabel("rhos")
plt.ylabel("Average Moves to Equilibrium")
plt.grid(True)
plt.show()'''















'''import numpy as np
import matplotlib.pyplot as plt
import random
#i want to find the cluster's of each agent separately 
from scipy.ndimage import label


Bm=0.75
def grid(ratio0):
    N=60
    ratio1=(1-ratio0)/2
    ratio2=(1-ratio0)/2
    #ratio of empty and 1 and 2
    values = [0, 1, 2]
    weights = [ratio0, ratio1, ratio2] 
    # Create grid
    grid = np.random.choice(values, size=(N,N), p=weights)
    return grid
        

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
    return (same / (diff+same)) >= Bm


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
                
            
def move_agents(grid, empty, unhappy):
    random.shuffle(empty)
    random.shuffle(unhappy)
    #we need random choices!
    for agent_pos, empty_pos in zip(unhappy, empty):
        ai, aj = agent_pos
        ei, ej = empty_pos
        grid[ei, ej] = grid[ai, aj]
        #leave empty behind
        grid[ai, aj] = 0  

    return grid          



def simulate(grid):
    max_steps=500
    history = [grid.copy()]
    moves=0
    for step in range(max_steps):
        empty, unhappy = find_unhappy(grid)
        if not unhappy:
            #print(f"Equilibrium reached at step {step}")
            break
        grid = move_agents(grid, empty, unhappy)
        history.append(grid.copy())
        moves+=1
    
    return history, moves

'''#check the new import use:
grid = np.array([
    [1, 1, 0, 0],
    [1, 0, 0, 2],
    [0, 0, 2, 2],
    [1, 2, 2, 0]])
#number of labels
labeled_grid1, num1 = label(grid == 1)
labeled_grid2, num2 = label(grid == 2)
print(labeled_grid1)
print(labeled_grid2)
'''
def segregation(grid, rho0):
    N = grid.shape[0]

    # Skip calculation if rho is 1 (entire grid is empty)
    if rho0 == 1:
        return np.nan  # Or return a large number or skip this case

    nc = []
    labeled_grid1, num1 = label(grid == 1)
    labeled_grid2, num2 = label(grid == 2)
    
    for labels in range(1, num1 + 1):
        cluster_size = np.sum(labeled_grid1 == labels)  # Count the cells in the current cluster
        nc.append(cluster_size)

    # Label the clusters for Group 2 (agents = 2)
    for labels in range(1, num2 + 1):
        cluster_size = np.sum(labeled_grid2 == labels)  # Count the cells in the current cluster
        nc.append(cluster_size)

    # Calculate the density of empty cells (rho)
    rho = np.count_nonzero(grid == 0) / (N * N)

    # Segregation coefficient formula
    segregation = (2 / (N ** 4 * (1 - rho) ** 2)) * sum([size ** 2 for size in nc])

    return segregation


rhos = np.linspace(0.1, 0.85, 25)
all=[]
for rho in rhos:
    g = grid(rho)
    segregation_coefficients= []
    for i in range(50):
        history, _ = simulate(g) 
        segregation_coefficient =segregation(history[-1], rho) 
        segregation_coefficients.append(segregation_coefficient)
    all.append(np.mean(segregation_coefficients))


plt.plot(rhos, all, marker='o', linestyle='-', color='b')
plt.xlabel("rho")
plt.ylabel("S")
plt.grid(True)
plt.show()'''




















