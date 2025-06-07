import numpy as np
import matplotlib.pyplot as plt
import random
#i want to find the cluster's of each agent separately 
from scipy.ndimage import label
import numba



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

@numba.jit(nopython=True)
def happiness(grid, i,j,Bm):
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

@numba.jit(nopython=True)
def find_unhappy(grid, Bm):
    unhappy=[]
    empty=[]
    N=grid.shape[0]
    for i in range(N):
        for j in range(N):
            if grid[i,j]==0:
                empty.append((i,j))
            elif not happiness(grid, i,j, Bm):
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



def simulate(grid,Bm):
    max_steps=500
    history = [grid.copy()]
    moves=0
    for step in range(max_steps):
        empty, unhappy = find_unhappy(grid,Bm)
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

def segregation(grid,rho0):
    N = grid.shape[0]
    #just add the size of each cluster that you find to it :)
    nc=[]
    labeled_grid1, num1 = label(grid == 1)
    labeled_grid2, num2 = label(grid == 2)
    for labels in range(1,num1+1):
        #you will have a boolean martix and then you can count all the indivisual cells with the same label
        cluster_size=np.sum(labeled_grid1==labels)
        nc.append(cluster_size)

    #now we need the same treatment for agent 2
    for labels in range(1,num2+1):
        #you will have a boolean martix and then you can count all the indivisual cells with the same label
        cluster_size=np.sum(labeled_grid2==labels)
        nc.append(cluster_size)


    total_agents = (N ** 2) * (1 - rho0)
    segregation = sum([size ** 2 for size in nc]) / (total_agents ** 2)
    
    return segregation

    
rhos=[0.10, 0.03, 0.18, 0.26]
for rho in rhos:
    Bms = np.linspace(0, 1.0, 15)
    segregation_coefficients = []
    for Bm in Bms:
        segregation_coefficients_run = [] 
        for i in range(20):  
            g = grid(0.2)
            history, _ = simulate(g,Bm)  
            segregation_coefficient = segregation(history[-1], rho) 
            segregation_coefficients_run.append(segregation_coefficient) 
        segregation_coefficients.append(np.mean(segregation_coefficients_run))
    
    
    plt.plot(Bms, segregation_coefficients, label=f"rho={rho}")
    plt.xlabel("Bm")
    plt.ylabel("S")
    plt.grid(True)
    plt.legend()
plt.show()
