import numpy as np
import random as r
import matplotlib.pyplot as plt
#now we will work with some interaction with neighbors
#again we have a 1D surface
'''x=np.arange(0,200,1)
#for each house we need to determine the height
height=np.zeros(200)
#we also need a time_snap to save the dynamic after a certain amount of time
N_samples=20000
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
plt.show()'''
#put it all in a function so we can call it for averaging
def Simulation(N,L):
    #now lets work on fits
    #we stil have x and h according to arbitrary L=200
    x_co=np.arange(0,L,1)
    h=np.zeros(L)
    #number of samples
    t_snap=[]
    n = 1
    #creating good time spacing like other reports:)
    while True:
        tn = int(1000 * (1.2) ** n) 
        if tn >= N:  
            break
        t_snap.append(tn)
        n=n+1

    h_snapshot=[]
    #i will save the h in different times

    for i in range(N):
        #choose a house
        r_house=r.randint(0,L-1)
        #check the neighbors
        #we have 200 houses, the house at 0 and 200 should be neighbours. for this we have to link 0 and 199 with a periodic boundary.
        #module cam do this for us easily because it has affect on the two end houses naturally
        #print(-1%200) is 199 wich is corrrect!
        #for 199=> 200%200 is 0 which is correct again :)
        min_height=min(h[r_house],h[(r_house+1)%L],h[(r_house-1)%L])
        #now lets see this belongs to which house!
        if h[r_house]==min_height:
            h[r_house]=h[r_house]+1
        elif h[(r_house+1)%L]==h[(r_house-1)%L]==min_height:
            #choose randomly between them
            idx= r.choice([(r_house-1)%L, (r_house+1)%L]) 
            h[idx]=h[idx]+1
        elif h[(r_house-1)%L]==min_height:
            h[(r_house-1)%L]=h[(r_house-1)%L]+1
        else:
            h[(r_house+1)%L]=h[(r_house+1)%L]+1
            
        
        #now lets save snap shots!
        if np.isin(i, t_snap):
            h_snapshot.append(h.copy())
    #print(h_snapshot)
    #now lets calculate the mean and var
    average_snap=[]
    for n in range(len(t_snap)):
        #mean :)
        avr=np.mean(h_snapshot[n])
        average_snap.append(float(avr))
    #print(average_snap)
    #now for std
    w=[]
    for c in range(len(t_snap)):
        var=np.sqrt(np.mean((h_snapshot[c])**2)-(np.mean(h_snapshot[c]))**2)
        w.append(float(var))
    return t_snap, w
#we should take average of multiple runs!

Var_all = []

for i in range(12):
    sim = Simulation(400000,200)
    Var_all.append(sim[1])
#averaging over all runs
meaning=np.mean(Var_all, axis=0)
#b,a= np.polyfit(np.log(time_snapshot), np.log(w), 1)
    
t=sim[0]
plt.scatter(np.log(t), np.log(meaning), marker='o')
plt.title("w and t for 200000 samples")
plt.xlabel("logt")
plt.ylabel("logw")
plt.show()
            


