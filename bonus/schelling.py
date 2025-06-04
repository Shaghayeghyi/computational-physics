import numpy as np
import matplotlib.pyplot as plt
import random



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


def happiness(grid, i,j, Bm):
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


Bms=np.linspace(0.1, 1.0, 10)
g=grid()
moving=[]
for Bm in Bms:
    means=[]
    for i in range(8):
            G=g.copy()
            _, moves=simulate(G)
            means.append(moves)
    moving.append(np.mean(means))
    

plt.plot(Bms, moving, marker='o', linestyle='-', color='b')
plt.xlabel("Bm")
plt.ylabel("Average Moves to Equilibrium")
plt.grid(True)
plt.show()


'''from matplotlib.animation import FuncAnimation, PillowWriter
from IPython.display import HTML

# Create and simulate the grid
g = grid()
history = simulate(g)

# Set up the animation
fig, ax = plt.subplots(figsize=(10, 8))
cmap = plt.cm.colors.ListedColormap(['white', 'blue', 'red'])
im = ax.imshow(history[0], cmap=cmap)
def update(frame):
    im.set_data(history[frame])
    ax.set_title(f"Step {frame}")
    return [im]

ani = FuncAnimation(fig, update, frames=len(history), interval=300, blit=True)
ani.save("schelling_model.gif", writer="pillow", fps=5, dpi=100)
plt.close() 
HTML(ani.to_jshtml()) 
#use plt.show() if not in jupyter'''
