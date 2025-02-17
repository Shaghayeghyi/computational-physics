import numpy as np
import matplotlib.pyplot as plt

#This is two D plot. so we will create a line with a specific lenght using 2 D array
#The initial line
pi=np.array([0,0])
pf=np.array([1,0])


#splitting it in 3 segments!
#pi is the start point and pf is the end of the line therefore p1=pi+1/3(pf-pi) and p2=pi+2/3(pf-pi)
'''p1=pi+1/3*(pf-pi)
p2=pi+2/3*(pf-pi)
print(p1,p2)

#now i should split the middle part in two!
pm=(p2-p1)/2'''

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

#now that we have an algorithm lets make some for loops to repeat this code for each new segment and create a koch curve:)
#for doing so, we fisrt should have a iteration number so we will stop the algorithm at some point. if the iteration steps is 0 then we are left
#with pi and pf only

def fractal(pi,pf,iteration):
    #we have an aray of 2D point that we want to draw.
    points=[]
    if iteration==0:
        #no changes
        points=[pi,pf]
    else:
        points=[pi,pf]
        for n in range(iteration):
            #this is to keep every point sorted correctly
            new_points=[]
            #now we will have some new points by each step.
            #for example in the first step we will create three new points
            #we need these points to create the base line for the ;next; step
            for m in range(len(points)-1):
                #for two point we have one line for 5 points we have 4 line and..
                origin=points[m]
                finish=points[m+1]
                #each line is created with two adjacent points
                #for each line we made three segments within
                p1=origin+1/3*(finish-origin)
                p2=origin+2/3*(finish-origin)
                #now the 60 degree rotated part
                #the order is important for us or maybe we can use some sort algorithm and do not bother!
                R=rotation(p2,p1,60)
                new_points.append(origin)
                new_points.append(p1)
                new_points.append(R)
                new_points.append(p2)
            new_points.append(finish)
            points=new_points
    return points                
                
            
'''R1=rotation(p2,p1,60)
R2=rotation(pm,p2,-60)'''
#now we will draw all of the sorted points we have
plot_data=np.array(fractal(pi,pf,2))
plt.figure(figsize=(6,6))
plt.plot(plot_data[:,0],plot_data[:,1])
#this little guy helped me with axis symmetry :)
plt.axis('equal')
plt.title('snowflake!')
plt.legend()
plt.show()
