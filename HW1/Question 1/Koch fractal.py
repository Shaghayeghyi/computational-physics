import numpy as np
import matplotlib.pyplot as plt

#This is two D plot. so wil create a line with a specific lenght using 2 D array
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
