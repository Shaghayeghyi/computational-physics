import numpy as np
import matplotlib.pyplot as plt
from random import random,randint
#we want to look at pecolation using HK algorithm
#we have a top left check system so we will get rid of on row and column
#we need an array so save the size of clusters
#we need a plane LxL
#we should create a function that leads us to the root:)
L=10
p=0.3

def Plane(L,p):
    plane = np.zeros((L,L+1),dtype = int)#L+2 for side's column
    plane[:,0]=1
    count=0
    for j in range(1,L-1):
        for i in range(1,L-1):
            random_p=random()
            if random_p<p:
                plane[i,j]=1
                count=count+1
    return plane,count

print(Plane(10,0.5))


def HK(plane):
    grid,count=plane
    n_rows, n_columns = grid.shape
    #create a grid to put the labels insdie according to grid
    label_grid = np.zeros((n_rows, n_columns), dtype=int)
    label_counter=0
    labels = np.arange(count+1)

    
    def find_root(label,array):
        if label == array[label]:
            return label
        else:
            array[label] = find_roots(array[label],array)
            return array[label]


    
    for j in range(1,n_columns):
        for i in range(n_rows):
            
            #look for on sites
            if grid[i,j]!=0:
                #look for its left and top neighbor
                top_n=grid[i-1,j]
                left_n=grid[i,j-1]
                #now we have three ways
                if top_n==0 and left_n==0:
                    #new cluster
                    label_grid[i,j]=label_counter+1
                    label_counter+=1
                    
                elif top_n==0 and left_n!=0:
                    label_grid[i,j]=find_root(left_n,labels)
                    

                elif top_n!=0 and left_n==0:
                    label_grid[i,j]=find_root(top_n,labels)
                    

                else:
                    root_L=find_root(left_n,labels)
                    root_T=find_root(top_n,labels
                                     )
                    min_label=min(root_L,root_T)
                    max_label=max(root_L,root_T)
                    label_grid[i,j]=min_label
                    labels[max_label]=min_label
    return label_grid
                    
                    
                    
print(HK(Plane(10,0.5)))
    

    

                    
                    
                    
            
