import numpy as np
import matplotlib.pyplot as plt
from random import randint,random

#simulating random walk in 2D
from random import random

def random_walk2():
    current_position = (0, 0)
    position_copy = []

    iteration = 100
    for i in range(iteration + 1):
        rand = random()

        if rand < 1/4:
            #right
            current_position = (current_position[0] + 1, current_position[1])  
            
        elif rand < 2/4:
            
            #up
            current_position = (current_position[0], current_position[1] + 1)
        elif rand < 3/4:
            
            #down
            current_position = (current_position[0], current_position[1] - 1) 
            
        else:
            
            #left
            current_position = (current_position[0] - 1, current_position[1])  

        if i % 10 == 0:
            position_copy.append(current_position)
            
    return position_copy
#lets run this code for 100 times
R2_all=[]
run=100000

for i in range(run):
    R2=np.zeros(11)
    #i will call this function run times
    positions=random_walk2()
    #each time i need to calculate r squared and get the mean
    for index , (x,y) in enumerate(positions):
        R2[index]=(x**2+y**2)
    R2_all.append(R2)

R2_all=np.mean(R2_all, axis=0)

#copy from past
time=list(range(0,101,10))
time=np.array(time)
plt.figure(figsize=(10, 5))
plt.scatter(time, R2_all, label='simulation')
(slope, intercept), (SSE,), *_ = np.polyfit(time, R2_all , 1, full=True)
fit= slope*time+intercept
plt.plot(time, fit , label=f'fit, the slope is{slope}')
plt.xlabel('Iteration')
plt.ylabel('mean r^2')
plt.legend()
plt.show()

print(SSE)   
