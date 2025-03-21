import numpy as np
import matplotlib.pyplot as plt
from random import randint,random

#define tale

def tale(p,position):
    start=position
    death_time=0
    x=start

    while 0<x<20:

        rand=random()

        if rand<p:
            x=x+1
            death_time=death_time+1
        else:
            x=x-1
            death_time=death_time+1
    return death_time

run=100000
mean_result=[]
x_range = np.arange(0, 21)
for j in x_range:
    run_result=[]
    for i in range(run):
        p=0.5
        TD=tale(p, j)
        run_result.append(TD)
    mean_result.append(np.mean(run_result))
    
a,b,c = np.polyfit(x_range,mean_result,deg=2)#fit of a degree 2 polynomial ax^2+bx+c

fit=a*(x_range)**2+b*x_range+c

plt.figure(figsize=(10, 5))
plt.scatter(x_range,mean_result , label='average death time')
plt.plot(x_range,fit, label=f'fit {a}x^2+{b}x+{c}')
plt.xlabel('x')
plt.ylabel('time')
plt.legend()
plt.show()
