import numpy as np
import matplotlib.pyplot as plt
import math as m

#alright we need to create a triangle
#we need three coordinate in a 2D world
p1=np.array([0,0])
p2=np.array([1,0])
#the apex of equilateral Triangle
p3=np.array([1/2,m.sqrt(3)/2])
#get the set of coordinates to describe the T
tr=np.array([p1,p3,p2,p1])

plt.plot(tr[:,0], tr[:,1])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Triangle")
plt.grid()
plt.show()
