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
    plane = np.zeros((L+2,L+2),dtype = int)#L+2 for side's column
    plane[:,0]=1
    plane[:,-1]=100
    count=0
    for j in range(1,L+1):
        for i in range(1,L+1):
            random_p=random()
            if random_p<p:
                plane[i,j]=1
                count=count+1
    return plane,count
#the plane is correct
#print(Plane(10,0.5))


def HK(plane):
    grid,count=plane
    #grid=grid[1:-1,1:-1]
    n_rows, n_columns = grid.shape
    L=n_rows-2
    #create a grid to put the labels insdie according to grid
    label_grid = np.zeros((n_rows, n_columns), dtype=int)
    label_counter=0
    labels = np.zeros(count+2,dtype=int)

    
    def find_root(label,array):
        if label == labels[label]:
            return label
        else:
            array[label] = find_root(array[label],array)
            return array[label]

    
    for j in range(1,L+1):
        for i in range(1,L+1):
            #we look at a square grid and don't get out of bound
            #look for on sites
            if grid[i,j]!=0:
                #look for its left and top neighbor
                top_n=label_grid[i-1,j]
                left_n=label_grid[i,j-1]
                #now we have three ways
                if top_n==0 and left_n==0:
                    #new cluster
                    label_counter+=1
                    label_grid[i,j]=label_counter
                    labels[label_counter] = label_counter
                    
                    
                elif top_n==0 and left_n!=0:
                    #link both to root
                    label_grid[i,j-1]=find_root(left_n,labels)
                    label_grid[i,j]=find_root(left_n,labels)
                    

                elif top_n!=0 and left_n==0:
                    #link both to root
                    label_grid[i-1,j]=find_root(top_n,labels)
                    label_grid[i,j]=find_root(top_n,labels)
                    

                else:
                    #compare labels
                    root_L=find_root(left_n,labels)
                    root_T=find_root(top_n,labels)
                    label_grid[i - 1][j] = root_T
                    label_grid[i,j - 1] = root_L
                    label_grid[i,j] = root_L
                    
                    if root_L != root_T:
                        #unite roots
                        labels[root_T] = root_L
                        
                 
    for j in range(1,L+1): 
        for i in range(1,L+1):
            label_grid[i, j] = find_root(label_grid[i, j],labels)
        
            
    return label_grid
                    
                    
im=HK(Plane(10,0.5))                   
print(im)
plt.imshow(im)   
plt.show()

    

                    
                    
                    
            
