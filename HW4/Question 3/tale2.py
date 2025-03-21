import numpy as np
import matplotlib.pyplot as plt
from random import randint,random

def tale2(P, starting_position):
    
    probability_array = np.zeros(21)
    probability_array[starting_position] = 1
    total=0
    p = P
    q = 1 - p
    death_time = 0
    p_out=0.0001
    
    while np.sum(probability_array[1:-1]) >p_out:
        new_probability = np.zeros_like(probability_array, dtype=np.float64)

        #boundary
        new_probability[0] = probability_array[0]
        new_probability[20] = probability_array[20]
        
        #each row's probs
        for j in range(1, len(probability_array) - 1):
            #left
            new_probability[j - 1] += q * probability_array[j]
            #right
            new_probability[j + 1] += p * probability_array[j]
            
        probability_array = new_probability
        
        #print(probability_array)
        #print(f'step {death_time}')
        death_time += 1
    
    
    return death_time

    
#print(tale2(0.5,10))   
#just used the last question no need for all this really
run=1
mean_result1=[]
starting_positions=np.arange(0,21)

for x in starting_positions:
    run_result1=[]
    for i in range(run):
        p=0.5
        TD=tale2(p,x)
        run_result1.append(TD)
    mean_result1.append(np.mean(run_result1))


a,b,c = np.polyfit(starting_positions,mean_result1,deg=2)#fit of a degree 2 polynomial ax^2+bx+c

fit=a*(starting_positions)**2+b*starting_positions+c

plt.figure(figsize=(10, 5))
plt.scatter(starting_positions,mean_result1 , label='average death time')
plt.plot(starting_positions,fit, label=f'fit {a}x^2+{b}x+{c}')
plt.xlabel('x')
plt.ylabel('time')
plt.legend()
plt.show()
 
