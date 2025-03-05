import numpy as np
import random as r
import matplotlib.pyplot as plt
from scipy.stats import linregress
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
        height[(rand_house+1)%200]=height[(rand_house+1)%==200]+1
        
    
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


'''#put it all in a function so we can call it for averaging
def Simulation(N,L):
    #now lets work on fits
    #we stil have x and h according to arbitrary L=200
    x_co=np.arange(0,L,1)
    h=np.zeros(L)
    #number of samples
    #creating good time spacing like other reports:)
    #more efficient version
    #how many time ranges you want?
    stop=45
    t_snap=np.array([N/(1.2**n) for n in range(stop,0,-1)],int)
    #better spacing may help :"
    #t_snap =np.unique(np.round(np.logspace(1, np.log10(N), stop)).astype(int))

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
        #more efficient no need for % for the last one
        min_height=min(h[r_house],h[(r_house+1)%L],h[(r_house-1)%L])
        #now lets see this belongs to which house!
        if h[r_house]==min_height:
            h[r_house]+=1
        elif h[(r_house+1)%L]==h[(r_house-1)%L]==min_height:
            #choose randomly between them
            idx= r.choice([(r_house-1)%L, (r_house+1)%L]) 
            h[idx]+=1
        elif h[(r_house-1)%L]==min_height:
            h[(r_house-1)%L]+=1
        else:
            h[(r_house+1)%L]+=1
            
        
        #now lets save snap shots!
        if i in t_snap:
            h_snapshot.append(h.copy())
    #print(h_snapshot)
    #now lets calculate the mean and var
            #maybe more efficient:(
    average_snap = [np.mean(snap) for snap in h_snapshot]
    w = [np.sqrt(np.var(snap, ddof=1)) for snap in h_snapshot]
    
    
    
        
    return w, average_snap
#okay now lets test out code for w and
#print(Simulation(40000,200))
all_data=[]
#how many runs:
j=25

for k in range(j):
    wk,meank=Simulation(4000000,400)
    print(k)
    all_data.append(wk)'''
    
'''print("data 1")
t_shot, W1, av1=Simulation(4000000,200)
print("data 2")
t_shot, W2, av2=Simulation(4000000,200)
print("data 3")
t_shot, W3, av3=Simulation(4000000,200)
print("data 4")
t_shot, W4, av4=Simulation(4000000,200)
#now we have 4 data set we just need to average them and plot to lines for them
all_data = np.array([W1, W2, W3, W4])'''


'''stop=45
t_shot=np.array([4000000/(1.2**n) for n in range(stop,0,-1)],int)
# Compute the average across all datasets
average_W = np.mean(all_data, axis=0)

#we want to plot in the lograrithm scale
#we could do this or just plot and log log diagram
log_t = np.log(t_shot)
log_w = np.log(average_W)

#we kinda are able to see the saturation point so we can split our data in two different parts according to that
split_index = int(0.65* len(log_t))  
#we wll fit a line to each of these to phases
slope1, intercept1, _, _, _ = linregress(log_t[:split_index], log_w[:split_index])
line1 = slope1 * log_t + intercept1
#btw we do not need things  such as regression and error right now so we ignore them basically!
slope2, intercept2, _, _, _ = linregress(log_t[split_index:], log_w[split_index:])
line2 = slope2 * log_t + intercept2

#just let lines connect and find the critical point
critical_log_t = (intercept2 - intercept1) / (slope1 - slope2)
critical_log_w = slope1 * critical_log_t + intercept1
#we need this out nex plot and report for alpha
print(slope1, "is beta")
print(critical_log_w ,"is ln Ws")
# Plot results
plt.scatter(log_t, log_w, marker='o', label="Data")
#plotting with limit is a better visiulization imo :)
plt.plot(log_t[:split_index], line1[:split_index], 'r--', label="Growth Phase Fit")
plt.plot(log_t[split_index:], line2[split_index:], 'g--', label="Saturation Phase Fit")
plt.xlabel("log t")
plt.ylabel("log w")
plt.legend()
plt.show()'''

lenght=[200,300,350,400]
beta=[0.25,0.22,0.25,0.26]
lenght=np.array(lenght)
logL=np.log(lenght)

lnws=[0.91 ,1.14, 1.17 ,1.15]
lnws=np.array(lnws)
print("mean of beta is:",np.mean(beta))
slope, intercept, _, _, _ = linregress(logL, lnws)
plt.scatter(logL, lnws)
plt.plot(logL,slope*logL+intercept)
plt.xlabel("log L")
plt.ylabel("log ws")
plt.show()
print("alpha is",slope)


