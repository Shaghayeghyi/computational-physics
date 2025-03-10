import numpy as np
import matplotlib.pyplot as plt
from random import random,randint

#at first we need to create a LxL lattice full of zeros
#then we will assing a random number betwwen (0,1) to each house
def random_on(L,p):
    Lattice=np.zeros((L, L), dtype=int)
    random_p=np.random.rand(L, L)
    #go through lattice
    for i in range(L):
        for j in range(L):
            if random_p[i,j]<p:
                Lattice[i,j]=1
            else:
                Lattice[i,j]=0
    return Lattice
            

#for seeing whether the percolation happend or not, we will start from on sites and the left
#for each one we will look at the top, down and right neighbor for a path
#after visiting each site, we will marke it to not go through that again
#by moving to right and reaching the very right column with number one, we will assume that the percolation happened

def find_path(Lattice):
    L=10
    p=0.5
    left_column=Lattice[:,0]
    #not seen sites are zero
    paths_seen=np.zeros((L, L), dtype=int)
    #start from the 1s on the first columns and add every neighbor with 1
    paths=[]
    for i in range(L):
        if left_column[i]==1:
            paths.append((i,0))
            paths_seen[i,0]=1 #seen!

    null=[]
    while paths!=null:
        #get rid of the last added site and work on its neighbors
            i,j = paths.pop()

            #percolation
            if j == L - 1:
                return 1


            neighbors = [(i, j + 1), (i - 1, j), (i + 1, j)]
            
            for m, n in neighbors:
                #the last condition helps us to not go back to checked paths
                if 0 <= m < L and 0 <= n < L and Lattice[m, n] == 1 and paths_seen[m,n]==0:
                    paths.append((m, n))
                    paths_seen[m,n]=1
                    
    return 0
        
#just checking
'''array=[(1,2),(6,7),(10,15)]
for i , j in array:
    print(i,j)
i,j=array.pop()
print(i,j)
print(array)'''
LL=random_on(10,0.5)
print(LL)
if find_path(LL)==1:
    print("we had percolation")
else:
    print("we had no percolation!")
    
plt.imshow(LL, cmap='Greys')
plt.show()
                    
            
