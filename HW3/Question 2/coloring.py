import numpy as np
import matplotlib.pyplot as plt
from random import random,randint
#we want to simulate percolation using coloring methods
#we have a LxL lattice once again but the most lef and right column have initial values:

def lattice(L,p):
    color=2
    #create 2D array with all zeros at first
    plane=np.zeros((L+2,L+2))
    #give number 1 to the left column
    left_column=plane[:,0]=1
    int_max=100
    right_column=plane[:,-1]=int_max
    #now lets check every house
    for j in range(1,L+1):
        for i in range(1,L+1):
            random_p=random()
            #print(random_p)
            if random_p<p:
                plane[i,j]=color
                color+=1
                #so we have a different color for the other houses
                #up down right left
                top_n=plane[i-1,j]
                left_n=plane[i,j-1]
                if top_n==0 and left_n==0:
                    #plane[i,j]=color
                    #color+=1
                    continue
                elif top_n!=0 and left_n==0:
                    plane[i,j]=top_n
                elif top_n==0 and left_n!=0:
                    plane[i,j]=left_n
                else:
                    min_color=min(top_n,left_n)
                    max_color=max(top_n,left_n)
                    plane[i,j]=min_color
                    for k in range(1,L+1):
                        for l in range(1,L+1):
                            if plane[l,k]==max_color:
                                plane[l,k]=min_color
    #Check for percolation
    percolation = 1 in plane[:, -2]
                        
            
    return plane ,percolation

image,percolation=lattice(10,0.65)
#print(image[:,:-1])
print(percolation)
plt.imshow(image[:,:-1], cmap='nipy_spectral')
plt.title(f"this is for L={10} and p={0.65}")
plt.show()
