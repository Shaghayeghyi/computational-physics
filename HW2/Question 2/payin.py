import numpy as np
import random as r
import matplotlib.pyplot as plt
#now we will work with some interaction with neighbors
#again we have a 1D surface
x=np.arange(0,200,1)
#for each house we need to determine the height
height=np.zeros(200)
#we also need a time_snap to save the dynamic after a certain amount of time
N_samples=200000
height_snapshot=[]
time_snapshot=[int(N_samples/4),2*int(N_samples/4),3*int(N_samples/4),N_samples-1]

for i in range(N_samples):
    #choose a house
    rand_house=r.randint(0,199)
    #check the neighbors
    #we have 200 houses, the house at 0 and 200 should be neighbours. for this we have to link 0 and 199 with a periodic boundary.
    #module cam do this for us easily because it has affect on the two end houses naturally
    #print(-1%200) is 199 wich is corrrect!
    #for 199=> 200%200 is 0 which is correct again :)
    minimum_height=min(height[rand_house],height[(rand_house+1)%200],height[(rand_house-1)%200])
    #now lets see this belongs to which house!
    if height[rand_house]==minimum_height:
        height[rand_house]=height[rand_house]+1
    elif height[(rand_house+1)%200]==height[(rand_house-1)%200] and minimum_height==height[(rand_house-1)%200]:
        #choose randomly between them
        index= r.choice([(rand_house-1)%200, (rand_house+1)%200]) 
        height[index]=height[index]+1
    elif height[(rand_house-1)%200]==minimum_height:
        height[(rand_house-1)%200]=height[(rand_house-1)%200]+1
    else:
        height[(rand_house+1)%200]=height[(rand_house+1)%200]+1
        
    
    #now lets save snap shots!
    if i in time_snapshot:
        height_snapshot.append(height.copy())
        
#now we can plot the height in different colors
plt.bar(x,height_snapshot[0], color='blue',alpha=0.6)
plt.bar(x,height_snapshot[1]-height_snapshot[0], color='red',alpha=0.6,bottom=(height_snapshot[0]))
plt.bar(x,height_snapshot[2]-height_snapshot[1], color='blue',alpha=0.6,bottom=(height_snapshot[1]))
plt.bar(x,height_snapshot[3]-height_snapshot[2], color='red',alpha=0.6,bottom=(height_snapshot[2]))
plt.title("deposition with 20000 samples")
plt.show()

