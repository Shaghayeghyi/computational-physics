import random
import numpy as np
import matplotlib.pyplot as plt

#i want to find every possible SAW with a lenght N and plot the results
#we will make it recursive and the output will be the count
all_visited=[]
#at first we have not visited anywhere
def all_SAW(N,x=0 ,y=0 , visited_sites=None):
    
    count=0
    if visited_sites is None:
        visited_sites=[(x,y)]
    #plane=np.zeros((2*N,2*N))
    
    if N==0:
        count=1
        return count #you can say one way possible
        
    else:
        #plane[x,y]=1 #visited
        shifts=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
        #if the neighbors are not vistied then we need to check all of them
        for shift in shifts:
            new_posx, new_posy=shift
            if shift not in visited_sites: #not visited
                new_visit=visited_sites.copy()
                new_visit.append((new_posx,new_posy))
                #plane[new_posx,new_posy]=1
                sub_count=all_SAW(N-1,new_posx,new_posy, new_visit)
                count+=sub_count
                
    return count
    
print(all_SAW(5,0,0,None))             
    
