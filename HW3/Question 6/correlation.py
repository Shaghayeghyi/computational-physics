import numpy as np
import matplotlib.pyplot as plt
from random import random,randint
#we need the pervoius functions

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
    #print("hello")
    #print(grid)
    n_rows, n_columns = grid.shape
    L=n_rows-2
    #create a grid to put the labels insdie according to grid
    label_grid = np.zeros((n_rows, n_columns), dtype=int)
    label_grid[:,0]=1
    label_grid[:,-1]=100
    label_counter=1
    labels = np.arange(count+2,dtype=int)
    #i should also add an array to save the size of clusters
    cluster_size = np.zeros(L * L)
    
    #now for saving the position of the sites with the same label, i need a dictionary
    clusterL_position={}
    for i in range(count+2):
        clusterL_position[i]=[]
    
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
                    
                    label_grid[i,j]=label_counter
                    labels[label_counter] = label_counter
                    cluster_size[label_counter] += 1
                    clusterL_position[label_counter].append((i,j))
                    label_counter+=1
                    
                    
                elif top_n==0 and left_n!=0:
                    #link both to root
                    label_grid[i,j-1]=find_root(left_n,labels)
                    label_grid[i,j]=find_root(left_n,labels)
                    clusterL_position[find_root(left_n,labels)].append((i,j))
                    cluster_size[find_root(left_n,labels)] += 1
                    

                elif top_n!=0 and left_n==0:
                    #link both to root
                    label_grid[i-1,j]=find_root(top_n,labels)
                    label_grid[i,j]=find_root(top_n,labels)
                    clusterL_position[find_root(top_n,labels)].append((i,j))
                    cluster_size[find_root(top_n,labels)] += 1
                    

                elif top_n!=0 and left_n!=0:
                    #compare labels
                    root_L=find_root(left_n,labels)
                    root_T=find_root(top_n,labels)
                    label_grid[i - 1][j] = root_T
                    label_grid[i,j - 1] = root_L
                    label_grid[i,j] = root_L
                    clusterL_position[find_root(left_n,labels)].append((i,j))
                    if root_L==root_T:
                        cluster_size[root_L] +=1
                    
                    if root_L != root_T:
                        #unite roots
                        #join two clusters and ignore the top one
                        cluster_size[root_L] = cluster_size[root_L] + cluster_size[root_T] + 1
                        cluster_size[root_T]=0
                        labels[root_T] = root_L
                        
                        
   
    for j in range(1,L+1): 
        for i in range(1,L+1):
            label_grid[i, j] = find_root(label_grid[i, j],labels)
            
    return label_grid, cluster_size, labels , clusterL_position
                    
                    
im,cluster_s,label, clusterP=HK(Plane(10,0.4)) 
print(clusterP)

def if_percolation(im):
    first_column=im[:,1]
    last_column=im[:,-2]
    #print(last_column)
    for i in last_column:
        for j in first_column:
            if i==j and i!=0:
                return 1
    return 0

#print(im)
#print(im[:-1,:-1])
plt.imshow(im[:-1,:-1])  
print(f'did we have percolation?{if_percolation(im)}')
#plt.title(f"this is for L={L} and p={p}")
plt.show()
print(cluster_s)

#now i want to use HK algorithm to work on the Q_inf
'''array= []

p_range = np.arange(0,1.05, 0.05)
L_range=[10,20,40,80,160]

for L in L_range:
    averag= []
    for p in p_range:
        #run this 100 time for each p
        #this is for L=10
        
        for i in range(100):
            sample_grid,cluster,_=HK(Plane(L,p))
            if if_percolation(sample_grid)==1:
                Q=max(cluster)
                
                array.append(Q)
            else:
                array.append(0)
        averag.append(np.average(array)/(L*L))
        array = []    
    plt.plot(p_range,averag,  label= f"this is for L = {L}")
    plt.xlabel("probability")
    plt.ylabel("Q_inf")
    plt.legend()

plt.show()'''

    
                    
                    
                    
            
