import numpy as np
import matplotlib.pyplot as plt

#This is two D plot. so we will create a line with a specific lenght using 2 D array
#The initial line
pi=np.array([0,0])
pf=np.array([1,0])


#splitting it in 3 segments!
#pi is the start point and pf is the end of the line therefore p1=pi+1/3(pf-pi) and p2=pi+2/3(pf-pi)
p1=pi+1/3*(pf-pi)
p2=pi+2/3*(pf-pi)
'''print(p1,p2)'''

#now i should split the middle part in two!
pm=(p2-p1)/2

#the two lines p1-pm and pm-p2 should rotate 60 degrees
#I should create a rotation function for me to do this.

def rotation(R_end, R_origin, tetha):
    degree=np.radians(tetha)
    #define a the typical rotation matrix for a 2D space :)
    R=np.array([[np.cos(degree), -np.sin(degree)],[np.sin(degree),  np.cos(degree)]])
    #alright now we define our line of interest
    l=R_end-R_origin
    #lets do the rotation
    return (np.dot(R,l)+R_origin)

R1=rotation(p2,p1,60)
R2=rotation(pm,p2,-60)
plot_data=np.array([pi,p1,R1,p2,pf])

plt.figure(figsize=(6,6))
plt.plot(plot_data[:,0],plot_data[:,1])
plt.legend()
plt.show()
