import numpy as  np
import matplotlib.pyplot as plt
import math as m

#we will again begin with a line
pi=np.array([0,0])
pf=np.array([1,0])
'''#we will also have a middle part
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
plt.show()'''

#I better work toward the two functions the problem wnats
#we will start by a line with unit lenght
#we should scale this live by 1/sqrt2 and rotate it 45 degree and create the red line
#we should also scale the line by 1/sqrt2 and rotate it 135 degree the move it by x=0 and y=0
#we will have the blue line
#we should repeat this process for our new lines so lets define these functions first

def R_45(l0):
    #45 degree rotation and scaling combined
    tetha=45
    degree=np.radians(tetha)
    #define a the typical rotation matrix for a 2D space :)
    Ro=(np.array([[np.cos(degree), -np.sin(degree)],[np.sin(degree),  np.cos(degree)]]))*1/m.sqrt(2)
    pi_new=np.dot(Ro,l0[0])
    pf_new=np.dot(Ro,l0[1])
    #new line
    l1=np.array([pi_new,pf_new])
    return l1
def RT_135(l0):
    #135 degree rotation and scaling and translation combined
    tetha=135
    degree=np.radians(tetha)
    T=np.array([1,0])
    #define a the typical rotation matrix for a 2D space :)
    Ro=(np.array([[np.cos(degree), -np.sin(degree)],[np.sin(degree),  np.cos(degree)]]))*1/m.sqrt(2)
    pi_new2=np.dot(Ro,l0[0])+T
    pf_new2=np.dot(Ro,l0[1])+T
    #we have line with 2 new endpoints
    l2=np.array([pf_new2,pi_new2])
    return l2

#I should also think about lines as in we need two endpoints for knowing it excatly. so i should create another array to represent a line
line0=np.array([pi,pf])
#this is now 2x2 the column 0 are the x and the column 1 is the y as usual:)
#the functions with get line0 and give back the two lines of step 1, then we should apply the functions on our new lines and go on
'''l1=R_45(line0)
l2=RT_135(line0)
print(l1)
print(l2)
data_plot=np.array([l1,l2])
plt.figure(figsize=(6,6))
plt.plot(l1[:,0],l1[:,1], c='b')
plt.plot(l2[:,0],l2[:,1], c='r')
#this little guy helped me with axis symmetry :)
plt.axis('equal')
plt.show()'''

#so things are working good, Step0 we have a line, step 2 we have 2 lines and for the next step we have to apply f1 and f2 two both of the lines

def fractal(l0, iteration):
    if iteration==0:
        plotting=l0
        plt.plot(plotting[:,0],plotting[:,1], c='b')
        return

    else:
        #we will define two lines
        l1=R_45(l0)
        l2=RT_135(l0)
        #now each line should act as an l0 and get impacted by f1 and f2
        #for instance on iteration 2,l0 will come to else and get divided to two section
        #each section with number iteration 1, so l1 and l2 will come to else and get divied to two (4 new lines)
        #then this 4 lines will get plotted on the if section
        fractal(l1,iteration-1)
        fractal(l2,iteration-1)
        return
    
fractal(line0,2)
plt.axis('equal')
plt.show()
