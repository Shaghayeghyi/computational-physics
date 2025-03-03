import numpy as np
import random as r
import matplotlib.pyplot as plt
from scipy.stats import linregress
#now we want to change the deposition manner
#the falling smaple will still look at left and right in a periodic manner
#it will detect hte maximum height and it will sit on its own x cordinate but at a height of (max(h(left)),max(h(right)))-height(rand_house)
#if the height of the r_house is the max itself then it will be added by one!
L=200
x=np.arange(0,L,1)
#we also need a time_snap to save the dynamic after a certain amount of time
#visiualization is a bit different from finding w and mean
#we need to detect the empty rooms beneath
#we need to see the empty space between the filled points right now so we will devide the plane in a 2D array of x rooms and maximum height possible
height_plane=np.zeros((2000,L), dtype=int)
#we also need another definition of height without caring about the empty spaces. just the height!
abs_h=np.zeros(L)
color=100
def Simulation(N_samples, L):
    stop=45
    h_snapshot=[]
    t_snapshot=np.array([N_samples/(1.2**n) for n in range(stop,0,-1)],int)
    for i in range (N_samples):
        #for each falling particle we choose a room(x)
        room_idx=r.randint(0,L-1)
        max_h= int(max(abs_h[room_idx],abs_h[(room_idx+1)%L],abs_h[(room_idx-1)%L]))
        if i in t_snapshot:
                h_snapshot.append(abs_h.copy())
        if abs_h[room_idx]==max_h:
            #change the the number 0 to color
            #height_plane[max_h+1,room_idx]=color
            abs_h[room_idx]+=1
        elif abs_h[(room_idx+1)%L]==max_h:
            #the absolute height of room_idx will be equal to right
            abs_h[room_idx]=max_h
            #height_plane[max_h,room_idx]=color
        elif abs_h[(room_idx-1)%L]==max_h:
            #the absolute height of room_idx will be equal to left
            abs_h[room_idx]=max_h
            #height_plane[max_h ,room_idx]=color
        
    average_snap = [np.mean(snap) for snap in h_snapshot]
    w = [np.sqrt(np.var(snap, ddof=1)) for snap in h_snapshot]
    return w, average_snap

#okay now lets test out code for w and
#print(Simulation(40000,200))
all_data=[]
all_data_mean=[]
#how many runs:
j=25

for k in range(j):
    wk,meank=Simulation(4000000,200)
    print(k)
    all_data.append(wk)
    all_data_mean.append(meank)
    
    
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
stop=45
t_shot=np.array([4000000/(1.2**n) for n in range(stop,0,-1)],int)
# Compute the average across all datasets
average_W = np.mean(all_data, axis=0)
average_mean=np.mean(all_data_mean, axis=0)
print(average_mean)
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
plt.show()
   
