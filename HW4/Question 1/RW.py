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
    for i in range(iteration+1):
        rand = random()
        #right and left
        if rand < p:
            current_position=current_position+1
        else:
            current_position=current_position-1
            
            
        
        if i%10==0: #make a copy
            position_copy.append(current_position)
             
    
    return position_copy
#average and Std of position

#lets run this code for 100 times

run=100000
run_av=[]
run_st=[]

for k in range(run):
    P=0.5
    current=random_walk(P)
    #print(averag)
    run_av.append(current)
    run_st.append(current)
run_st=np.array(run_st)
run_av=np.array(run_av)
run_av1=np.mean(run_av, axis=0)
run_st1=np.var(run_st, axis=0)


#print(len(st_positions))
#print(len(st_positions))
time=list(range(0,101,10))
time=np.array(time)
plt.figure(figsize=(10, 5))
plt.scatter(time,run_av1, label='Var Position')
slope, intercept = np.polyfit(time, run_av1, 1)
fit= slope*time+intercept
plt.plot(time, fit , label='fit')
plt.xlabel('Iteration')
plt.ylabel('average Position')
plt.legend()
plt.show()
print(f'this is for p={P}')
print(f'slope={slope}')
print(f'in theory we have slope={P-(1-P)}')
   

#print(len(st_positions))
#print(len(st_positions))
time=list(range(0,101,10))
time=np.array(time)
plt.figure(figsize=(10, 5))
plt.scatter(time,run_st1, label='Var Position')
slope, intercept = np.polyfit(time, run_st1, 1)
fit= slope*time+intercept
plt.plot(time, fit , label='fit')
plt.xlabel('Iteration')
plt.ylabel('Var Position')
plt.legend()
plt.show()
print(f'this is for p={P}')
print(f'slope={slope}')
print(f'in theory we have slope={4*P*(1-P)}')
   

