import numpy as np
import matplotlib.pyplot as plt
import math as m
import matplotlib.patches as patches

#alright we need to create a triangle
#we need three coordinate in a 2D world
p1=np.array([0,0])
p2=np.array([1,0])
#the apex of equilateral Triangle
p3=np.array([1/2,m.sqrt(3)/2])
#get the set of coordinates to describe the T
tr=np.array([p1,p3,p2])
'''T3=np.array([1/2,0])
print(tr+T3)'''

#i believe everything is very similar to the last code
#i need to work with three lines and i also need to work with three functions
#f1 should scale all 3 lines by 1/2
#f2 should do the same but transfer the new tri by (0, 1/2)
#f3 should scale too but it has a transfer by (1/4, sqrt3/4)
#another thing is that i need is a colored triangle to start with

# I will use Polygan for it
fig, ax = plt.subplots()
colored_T= plt.Polygon(tr, color='blue')
ax.add_patch(colored_T)
plt.show()



#it is not efficient to work with three lines. i will male the 3 point a single entity!
#my mind was stuck in the Dragon curve :))
def scale(tr):
    #scale by half
    return tr/2
def Transfer(l0):
    #scaling
    #one direction transfer
    T=np.array([1/2,0])
    return tr/2 +T
def Transfer2(l0):
    #scaling
    #one direction transfer
    T2=np.array([1/4,m.sqrt(3)/4])
    return tr+T2



