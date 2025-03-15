import numpy as np
import matplotlib.pyplot as plt
from random import random,randint
L=100
p=0.5
#we will start by a plane and a seed in the middle
#-1 means off and not visited
def clusterD(L,p):
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
    #cluster_size=1

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
        #now we need to check which one is blokced and which one is turned on and is in the new focus for us
        neighbors = np.unique(neighbors, axis=0)
        new_active_set=[]

        for i,j in neighbors:
            random_p=random()
            if random_p<p:
                plane[i,j]=1
                new_active_set.append((i,j))
            else:
                #block it
                plane[i,j]=0
        #so now we have the current actives
        current_active=new_active_set
        #add this to the turned on sites
        all_actives_list.extend(new_active_set)
    sum_coorx=0
    sum_coory=0
    cluster_size=len(all_actives_list)
    differencex=[]
    differencey=[]
    for x,y in all_actives_list:
        sum_coorx=sum_coorx+x
        sum_coory=sum_coory+y
    CM_x=sum_coorx/cluster_size
    CM_y=sum_coory/cluster_size
    for xx , yy in all_actives_list:
        difx=xx**2-CM_x**2
        dify=yy**2-CM_y**2
        differencex.append(difx)
        differencey.append(dify)
    differencex=np.sum(differencex)/cluster_size
    differencey=np.sum(differencey)/cluster_size
    Rg=np.sqrt(differencex+differencey)
        
        
        
    #print(all_actives_list)
    plt.imshow(plane, cmap='Grays')
    plt.show()
    return all_actives_list ,Rg, cluster_size
clusterD(L,p)

        

    
