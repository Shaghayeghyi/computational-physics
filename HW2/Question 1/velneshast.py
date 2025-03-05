import numpy as np
import random as r
import matplotlib.pyplot as plt
import pandas as pd
#we will be working onsome simple 1D surface growth process
#at first we need to create a surface on the x axis say with a lenght of 200
x=np.arange(0,200,1)
#print(x)
#now we need to create an array of length 200 to save the height of each x
#this is a 1D array to save the height which is 0 at first
height=np.zeros(200)
#we will also need a number of samples that will fall on the surface
N_samples=20000

#we need a for loop to go through every sample and find a place for it
time_splitted_sample=[]
#for future calculations
time_splitted_sample2=[]


for i in range(N_samples):
    if i==int(N_samples//4):
        time_splitted_sample.append(height.copy())
        time_splitted_sample2.append(height.copy())
    if i==2*int(N_samples//4):
        time_splitted_sample.append(height.copy()- time_splitted_sample[0])
        time_splitted_sample2.append(height.copy())
    if i==3*int(N_samples//4):
        time_splitted_sample.append(height.copy()- time_splitted_sample[0]-time_splitted_sample[1])
        time_splitted_sample2.append(height.copy())
    if i==N_samples-1:
        time_splitted_sample.append(height.copy()- time_splitted_sample[0]-time_splitted_sample[1]- time_splitted_sample[2])
        time_splitted_sample2.append(height.copy())
    #the question wants us to split our deposition into 4 differen timelines
    #so we will save each quarter of samples in a array
    rand_house=r.randint(0,199)
    #add a unit to the height of rand_house
    height[rand_house]=height[rand_house]+1
    
    
#print(x)
plt.bar(x,time_splitted_sample[0], color='blue',alpha=0.6)
plt.bar(x,time_splitted_sample[1], color='red',alpha=0.6,bottom=np.sum(time_splitted_sample[:1], axis=0))
plt.bar(x,time_splitted_sample[2], color='blue',alpha=0.6,bottom=np.sum(time_splitted_sample[:2], axis=0))
plt.bar(x,time_splitted_sample[3], color='red',alpha=0.6,bottom=np.sum(time_splitted_sample[:3], axis=0))
plt.title("this is for L=200 and 20000 samples")
plt.show()









'''#so the time_splitted_sample contains the lenght of each snapshot on deposition of our surface
#mean height general formula
#we also can save the height in more times
height_snapshot=[]
#for counter!
time_snapshot=[100,1000,10000,100000, N_samples-2]
h=np.zeros(200)
for m in range(N_samples):
   
    rand=r.randint(0,199)
    #add a unit to the height of rand_house
    h[rand]=h[rand]+1
    if np.isin(m, time_snapshot):
        height_snapshot.append(h.copy())

       
mean_height_snapshot=[]
for j in range(len(height_snapshot)):
    mean=np.mean(height_snapshot[j])
    mean_height_snapshot.append(float(mean))
print(mean_height_snapshot)    
#var
w=[]
av=[]
for l in range(len(height_snapshot)):
    means=np.mean(height_snapshot[l])
    var=np.sqrt(np.mean((height_snapshot[l])**2)-(np.mean(height_snapshot[l]))**2)
    av.append(float(means))
    w.append(float(var))
time=[100,1000,10000,100000, N_samples-2]
#print(av)
#print(time)

#print('hello')
#beta
df = pd.DataFrame({'time': time, 'mean': av})
print(df)


b,a= np.polyfit(np.log(time_snapshot), np.log(w), 1)
plt.plot(np.log(time_snapshot), np.log(w), marker='o', label=f"Slope= {b}")
plt.title("w and t for 200000 samples")
plt.xlabel("logt")
plt.ylabel("logw")
plt.legend(loc="upper left")



print("this is beta, our slope:",b)
plt.show()'''

