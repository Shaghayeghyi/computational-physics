import numpy as np
import matplotlib.pyplot as plt
from random import random,randint
L=100
p=0.6
#we will start by a plane and a seed in the middle
#-1 means off and not visited
def clusterD(L,p)
    #at first everything is unvisited
    plane = np.full((L+2,L+2),-2,dtype = int)
    #boundary
    plane[0, :] = 0
    plane[-1, :] = 0 
    plane[:, 0] = 0
    plane[:, -1] = 0
    
    middle=int(L/2)
    #turn it on
    activation=(middle,middle)
    plane[middle,middle]=1
    #the size of cluster is 1 now
    cluster_size=1

    current_active=[activation]
    null=[]
    all_actives_list=[activation]


    while current_active!=null:
        #find the not visited neighbors at first
        
        neighbors = []
        for row, col in current_active:
            
            if plane[row + 1, col] == -2:
                neighbors.append((row + 1, col))
            if plane[row - 1, col] == -2:
                neighbors.append((row - 1, col))
            if plane[row, col + 1] == -2:
                neighbors.append((row, col + 1))
            if plane[row, col - 1] == -2:
                neighbors.append((row, col - 1))

            

    plt.show()

