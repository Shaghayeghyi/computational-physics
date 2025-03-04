import numpy as np
import random as r
import matplotlib.pyplot as plt
from scipy.stats import linregress
'''#now we want to change the deposition manner
#the falling smaple will still look at left and right in a periodic manner
#it will detect hte maximum height and it will sit on its own x cordinate but at a height of (max(h(left)),max(h(right)))-height(rand_house)
#if the height of the r_house is the max itself then it will be added by one!
L=200
x=np.arange(0,L,1)
stop=35
#we also need a time_snap to save the dynamic after a certain amount of time
#visiualization is a bit different from finding w and mean
#we need to detect the empty rooms beneath
N_samples=200000
#we need to see the empty space between the filled points right now so we will devide the plane in a 2D array of x rooms and maximum height possible
height_plane=np.zeros((20000,L), dtype=int)
height_snapshot=[]
t_snapshot=np.array([5,10,20,30,40,50,60,70],int)
hp_snapshot=[]
color=100
#okay i need to change the initial condition
#all the rooms except the middle one have a very low value and it take a lot of time for them to grow
#so we have a main root
abs_h = np.full(L, -1000, dtype=int)

abs_h[100] = 100
#this is the base for creating a tree


for i in range (N_samples):
    #for each falling particle we choose a room(x)
    room_idx=r.randint(0,L-1)
    max_h=int(max(abs_h[room_idx],abs_h[(room_idx+1)%L],abs_h[(room_idx-1)%L]))
    if i in t_snapshot:
        #now i want a copy of the height for looking at the width
            hp_snapshot.append(abs_h.copy())
    if abs_h[room_idx]==max_h:
        abs_h[room_idx]+=1
        #change the the number 0 to color
        height_plane[max_h+1,room_idx]=color
    elif abs_h[(room_idx+1)%L]==max_h:
        #the absolute height of room_idx will be equal to right
        abs_h[room_idx]=max_h
        height_plane[max_h,room_idx]=color
    elif abs_h[(room_idx-1)%L]==max_h:
        #the absolute height of room_idx will be equal to left
        abs_h[room_idx]=max_h
        height_plane[max_h ,room_idx]=color
    #we also need to change the color every now and then in the visualization!
    if i%5000==0:
        color=-color
fig, ax = plt.subplots(figsize=(5, 5))
im = ax.imshow(height_plane, cmap="coolwarm")
ax.set_ylim(0, 250)
ax.set_xlim(0,200)
plt.title(" Tree with 20000 samples and L=200")
plt.show()

#now we want to find the most left and the most right house in each time shot
#we want to plot width with respect to time and look for scales. so an log log plot would be good!
#just checking my snapshot
#print(sum(hp_snapshot[3]))
#now for each snapshot i need to calculate the width
#distance is meaningful through columns
#I can work with abs height
#i will start from the first column and go through columns with the help of abs_h
distance_at_t=[]
for i in t_snapshot:
    #find the distance in each time
    x_start=0
    while abs_h[x_start]<=0:
        x_start+=1
    #now we have reached the first colored column
    #the very last column must start from x_start and start moving till we reach the next not_colored part
    x_finish=x_start
    while abs_h[x_finish]>=0:
        x_finish+=1
        if x_finish==L-1:
            #we do not want to go on after the end of system
            break
    distance_at_t.append(x_finish-x_start)
print(distance_at_t)'''

#okay here is the  code for width I am sorry about the mess:) most parts are just repeated
import numpy as np
import random as r
import matplotlib.pyplot as plt
from scipy.stats import linregress

# System size
L = 200
N_samples = 200000
hp_snapshot = []
# Initialization: Tree starts with -1000 everywhere except the center
abs_h = np.full(L, -1000, dtype=int)
abs_h[100] =100  # The root of the tree
#print(abs_h)
# Time snapshots (to analyze growth over time)
stop=30
t_snapshot = np.array([20000/(1.2**n) for n in range(stop,0,-1)],int)

# Deposition process
for i in range (N_samples):
        #for each falling particle we choose a room(x)
        room_idx=r.randint(0,L-1)
        max_h=int(max(abs_h[room_idx],abs_h[(room_idx+1)%L],abs_h[(room_idx-1)%L]))
        #print(max_h)
    
        if i in t_snapshot:
                hp_snapshot.append(abs_h.copy())
                #print(hp_snapshot)
        if abs_h[room_idx]==max_h:
            #change the the number 0 to color
            #height_plane[max_h+1,room_idx]=color
            abs_h[room_idx]+=1
        else:
            abs_h[room_idx]=max_h
            
# Calculate width of the tree at different time snapshots
distance_at_t=[]
for h in hp_snapshot:
    #print("this is abs h at time",i)
    #print(abs_h)
    #find the distance in each time
    x_start=0
    while h[x_start]<0:
        x_start+=1
        #print(x_start,"this is x start")
    #now we have reached the first colored column
    #the very last column must start from x_start and start moving till we reach the next not_colored part
    x_finish=x_start
    while x_finish < L-1 and h[x_finish] > 0:
        x_finish += 1
    distance_at_t.append(x_finish-x_start)
#print(distance_at_t)
#okay now we plot log log
log_t = np.log(t_snapshot)
log_w = np.log(distance_at_t)

slope, intercept, _, _, _= linregress(log_t, log_w)
line_fit=slope * log_t + intercept
plt.figure(figsize=(5, 5))
plt.scatter(log_t, log_w)
plt.plot(log_t,line_fit ,'r')
plt.xlabel("log t")
plt.ylabel("log w")
plt.title("Plot of Width")
plt.show()

print(f"slope is: {slope:}")




    
    


