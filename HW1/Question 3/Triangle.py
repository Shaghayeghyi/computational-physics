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

plt.show()



#it is not efficient to work with three lines. i will male the 3 point a single entity!
#my mind was stuck in the Dragon curve :))
def scale(tr):
    #scale by half
    return tr/2
def Transfer(tr):
    #scaling
    #one direction transfer
    T=np.array([1/2,0])
    return tr/2 +T
def Transfer2(tr):
    #scaling
    #one direction transfer
    T2=np.array([1/4,m.sqrt(3)/4])
    return tr/2+T2
#now this part of the code will be very similar to dragon. I will basically do some recursives

#no need for i because we do not want color change
def fractal(tr, iteration,ax):
    if iteration==0:
        colored_T= plt.Polygon(tr, color='blue')
        ax.add_patch(colored_T)
        return

    else:
        #alright we have 3 fs to apply :)
        tr1=scale(tr)
        tr2=Transfer(tr)
        tr3=Transfer2(tr)
        #we have a triangle, we will do 3 transformations and we will end up in step 1 then we will repeat this for every 3 new triangles
        #the iteration steps will clearly drop too :) just like dragon curve
        f1=fractal(tr1,iteration-1,ax)
        f2=fractal(tr2,iteration-1,ax)
        f3=fractal(tr3,iteration-1,ax)
        return
    
#attention we had to add ax to set the smaller triangles at the right place in our figure :)
fig, ax = plt.subplots()
fractal(tr,2,ax)
plt.axis('equal')
plt.show()





