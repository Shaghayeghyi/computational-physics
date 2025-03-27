#i need to create a SAW and for this having a place to save the visited sites is needed
import random
import numpy as np
import matplotlib.pyplot as plt

'''
#this is only a check
visited_sites=[]
x_start , y_start = 0,0
visited_sites.append((x_start,y_start))
print(visited_sites)'''

def SAW(max_step):
    visited_sites=[]
    positions=[]
    possible_moves=[]
    x_start , y_start = 0,0
    x=x_start
    y=y_start
    visited_sites.append((x,y))
    positions.append((x,y))
    for i in range(max_step):
        neighbors=[(x + 1, y),(x, y + 1),(x, y - 1),(x - 1, y)]
        for j in neighbors:
            if j not in visited_sites:
                possible_moves.append(j)
        x,y=random.choice(possible_moves)
        positions.append(new)
        visited_sites.append(new)
        
         
            
             
            
                           
           
    
