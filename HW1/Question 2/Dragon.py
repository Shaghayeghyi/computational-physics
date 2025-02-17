import numpy as  np
import matplotlib.pyplot as plt
import math as m

#we will again begin with a line
pi=np.array([0,0])
pf=np.array([1,0])
#we will also have a middle part
pm=(pf+pi)/2
#we again need a rotation but this time pm must rotate with respect to the origin
def rotation(R_end, R_origin, tetha):
    degree=np.radians(tetha)
    #define a the typical rotation matrix for a 2D space :)
    R=np.array([[np.cos(degree), -np.sin(degree)],[np.sin(degree),  np.cos(degree)]])
    #alright now we define our line of interest
    l=R_end-R_origin
    #we also have a scaling for the square
    #lets do the rotation
    return (np.dot(R,l))*m.sqrt(2)+R_origin
#so the rotated point by a right angle is like this
R=rotation(pm,pi,45)
data_plot=np.array([pi,R,pf])
plt.figure(figsize=(6,6))
plt.plot(data_plot[:,0],data_plot[:,1])
#this little guy helped me with axis symmetry :)
plt.axis('equal')
plt.show()

