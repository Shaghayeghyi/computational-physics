import numpy as np
import matplotlib.pyplot as plt
from random import random,randint
L=100
p=0.6
#we will start by a plane and a seed in the middle
#-1 means off and not visited
plane = np.full((L,L),-1,dtype = int)
middle=int(L/2)
#turn it on
activation=(middle,middle)
plane[middle,middle]=1

neighbors=[activation]
null=[]


while neighbors!=null:
    
    i,j=neighbors.pop()
    all_four_sides=[(i-1,j),(i,j-1),(i+1,j),(i,j+1)]
    #we will only work with on sites
    for k,l in all_four_sides:
        random_p=random()
        if random_p<p and 0<k<L and 0<l<L:
            if plane[k,l]!=0:
                plane[k,l]=1
                neighbors.append((k,l))
        elif 0<k<L and 0<l<L:
            #block
            plane[k,l]=0
        else:
            continue
plt.imshow(plane)

plt.show()

