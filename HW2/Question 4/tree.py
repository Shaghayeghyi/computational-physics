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
N_samples=20000
#we need to see the empty space between the filled points right now so we will devide the plane in a 2D array of x rooms and maximum height possible
height_plane=np.zeros((N_samples,L))
height_plane=np.zeros((2000,L), dtype=int)
height_snapshot=[]
time_snapshot=[int(N_samples/4),2*int(N_samples/4),3*int(N_samples/4),N_samples-1]
h_snapshot=[]
t_snapshot=[int(N_samples/4),2*int(N_samples/4),3*int(N_samples/4),N_samples-1]
color=100
#okay i need to change the initial condition
#all the rooms except the middle one have a very low value and it take a lot of time for them to grow
#so we have a main root
abs_h = np.full(L, -1000, dtype=int)

abs_h[100] = 0
#this is the base for creating a tree


for i in range (N_samples):
    #for each falling particle we choose a room(x)
    room_idx=r.randint(0,L-1)
    max_h=max(abs_h[room_idx],abs_h[(room_idx+1)%L],abs_h[(room_idx-1)%L])
    max_h= int(max(abs_h[room_idx],abs_h[(room_idx+1)%L],abs_h[(room_idx-1)%L]))
    if i in t_snapshot:
            h_snapshot.append(abs_h.copy())
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
plt.title(" Tree with 20000 samples and L=200")
plt.show()
