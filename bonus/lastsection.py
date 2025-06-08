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
    max_steps=400
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
from scipy.ndimage import label
grid = np.array([
    [1, 1, 0, 0],
    [1, 0, 0, 2],
    [0, 1, 2, 2],
    [1, 2, 2, 0]])

#moore neighbors
#number of labels
structure = np.ones((3, 3), dtype=int)
labeled_grid1, num1 = label(grid == 1, structure=structure)
labeled_grid2, num2 = label(grid == 2, structure=structure)
print(labeled_grid1)
print(labeled_grid2)
'''

'''def segregation(grid,rho0):
    N = grid.shape[0]
    #just add the size of each cluster that you find to it :)
    nc=[]
    #no moore neighbo according to the article
    structure = np.array([[0,1,0],[1,1,1],[0,1,0]])  # 4neighbor
    labeled_grid1, num1 = label(grid == 1, structure=structure)
    labeled_grid2, num2 = label(grid == 2 ,structure=structure)
    for labels in range(1,num1+1):
        #you will have a boolean martix and then you can count all the indivisual cells with the same label
        cluster_size=np.sum(labeled_grid1==labels)
        nc.append(cluster_size)

    #now we need the same treatment for agent 2
    for labels in range(1,num2+1):
        #you will have a boolean martix and then you can count all the indivisual cells with the same label
        cluster_size=np.sum(labeled_grid2==labels)
        nc.append(cluster_size)

        
    #segregation =((2 * np.sum([size**2 for size in nc]))/(N*N*(1-rho0))**2)
    # Count total agents of type 1 and 2
    num_agent1 = np.sum(grid == 1)
    num_agent2 = np.sum(grid == 2)
    total_agents = num_agent1 + num_agent2
    
    # Segregation formula adapted to true population count
    numerator = 2 * np.sum([size**2 for size in nc])
    denominator = (total_agents)**2
    
    segregation = numerator / denominator
        
    return segregation'''
#2 models of defining segragation weight    
def segregation(grid):
    #Agent 1
    #calculate the number of clusters each with its own label
    #article's suggestion for sturcture
    structure = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    labeled_1, num_1 = label(grid == 1, structure=structure)
    #size of clusters of agent 1
    sizes_1 = np.array([np.sum(labeled_1 == k) for k in range(1, num_1 + 1)])
    total_1 = np.sum(grid == 1)
    s1 = np.sum(sizes_1 ** 2) / (total_1 ** 2) if total_1 > 0 else 0

    # Agent 2
    #same rules
    labeled_2, num_2 = label(grid == 2, structure=structure)
    sizes_2 = np.array([np.sum(labeled_2 == k) for k in range(1, num_2 + 1)])
    total_2 = np.sum(grid == 2)
    s2 = np.sum(sizes_2 ** 2) / (total_2 ** 2) if total_2 > 0 else 0

    total_agents = total_1 + total_2
    weight_1 = total_1 / total_agents
    weight_2 = total_2 / total_agents
    
    return weight_1 * s1 + weight_2 * s2
    
rhos=[0.18, 0.26, 0.06]
for rho in rhos:
    Bms = np.linspace(0, 1.0, 15)
    segregation_coefficients = []
    for Bm in Bms:
        segregation_coefficients_run = [] 
        for i in range(10):  
            g = grid(rho)
            history, _ = simulate(g,Bm)  
            segregation_coefficient = segregation(history[-1]) 
            segregation_coefficients_run.append(segregation_coefficient) 
        segregation_coefficients.append(np.mean(segregation_coefficients_run))
    
    
    plt.plot(Bms, segregation_coefficients, label=f"rho={rho}")
    plt.xlabel("Bm")
    plt.ylabel("S")
    plt.grid(True)
    plt.legend()
plt.show()
