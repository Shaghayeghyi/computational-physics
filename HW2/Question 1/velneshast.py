import numpy as np
import random as r
import matplotlib.pyplot as plt
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
'''plt.bar(x,time_splitted_sample[0], color='blue',alpha=0.6)
plt.bar(x,time_splitted_sample[1], color='red',alpha=0.6,bottom=np.sum(time_splitted_sample[:1], axis=0))
plt.bar(x,time_splitted_sample[2], color='blue',alpha=0.6,bottom=np.sum(time_splitted_sample[:2], axis=0))
plt.bar(x,time_splitted_sample[3], color='red',alpha=0.6,bottom=np.sum(time_splitted_sample[:3], axis=0))

plt.show()'''
#so the time_splitted_sample contains the lenght of each snapshot on deposition of our surface
#mean height general formula
mean_height_snapshot=[]
for j in range(len(time_splitted_sample2)):
    mean=np.mean(time_splitted_sample2[j])
    mean_height_snapshot.append(float(mean))
#print(mean_height_snapshot)    
#var
w=[]
for l in range(len(time_splitted_sample2)):
    var=np.sqrt(np.var(time_splitted_sample2[l]))
    w.append(float(var))
time=[int(N_samples//4),2*int(N_samples//4),3*int(N_samples//4),N_samples-1]
#print(w)
plt.plot(np.log(time), np.log(w), marker='o')

print('hello')
#beta


b,a= np.polyfit(np.log(time), np.log(w), 1)
print(b)
plt.show()

