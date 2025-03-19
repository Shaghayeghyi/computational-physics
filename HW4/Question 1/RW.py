import numpy as np
import matplotlib.pyplot as plt
from random import randint,random

#simulating random walk
def random_walk(P):

    p=P
    q=1-p
    start_point=0
    current_position=0
    positions=[]
    positions.append(start_point)
    position_copy=[]
    iteration=100
    for i in range(iteration):
        rand = random()
        #right and left
        if rand < p:
            current_position=current_position+1
        else:
            current_position=current_position-1
            
        positions.append(current_position)
        if i%10==0: #make a copy
            position_copy.append(positions.copy())
             
    averag=[]
    Std=[]
    for j in range(len(position_copy)):
        averag.append(np.mean(position_copy[j]))
        Std.append(np.std(position_copy[j]))
    
    return averag, Std
#average and Std of position

#lets run this code for 100 times

run=10000
run_av=[]
run_st=[]

for k in range(run):
    P=0.2
    averag, Std=random_walk(P)
    run_av.append(averag)
    run_st.append(Std)


'''mean_positions=np.mean(run_av, axis=0)
plt.figure(figsize=(10, 5))
plt.scatter(np.arange(len(mean_positions)),np.mean(run_av, axis=0), label='Average Position')
slope, intercept = np.polyfit(np.arange(len(mean_positions)), mean_positions, 1)
fit= slope*np.arange(len(mean_positions))+intercept
plt.plot(np.arange(len(mean_positions)), fit , label='fit')
plt.xlabel('Iteration x10')
plt.ylabel('Position')
plt.legend()
plt.show()
print(f'this is for p={P}')
print(f'slope={slope}')'''

st_positions=np.mean(run_st, axis=0)
plt.figure(figsize=(10, 5))
plt.scatter(np.arange(len(st_positions)),np.mean(run_st, axis=0), label='Std Position')
slope, intercept = np.polyfit(np.arange(len(st_positions)), st_positions, 1)
fit= slope*np.arange(len(st_positions))+intercept
plt.plot(np.arange(len(st_positions)), fit , label='fit')
plt.xlabel('Iteration x10')
plt.ylabel('Position')
plt.legend()
plt.show()
print(f'this is for p={P}')
print(f'slope={slope}')

   

