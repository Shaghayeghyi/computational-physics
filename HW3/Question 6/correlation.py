import numpy as np
import matplotlib.pyplot as plt
from random import random,randint
from scipy.optimize import curve_fit

#we need the pervoius functions

def Plane(L,p):
    plane = np.zeros((L+2,L+2),dtype = int)#L+2 for side's column
    plane[:,0]=1
    plane[:,-1]=100
    count=0
    for j in range(1,L+1):
        for i in range(1,L+1):
            random_p=random()
            if random_p<p:
                plane[i,j]=1
                count=count+1
    return plane,count
#the plane is correct
#print(Plane(10,0.5))

def HK(plane):
    grid,count=plane
    #grid=grid[1:-1,1:-1]
    #print("hello")
    #print(grid)
    n_rows, n_columns = grid.shape
    L=n_rows-2
    #create a grid to put the labels insdie according to grid
    label_grid = np.zeros((n_rows, n_columns), dtype=int)
    label_grid[:,0]=1
    label_grid[:,-1]=100
    label_counter=2
    labels = np.arange(count+2,dtype=int)
    #i should also add an array to save the size of clusters
    cluster_size = np.zeros(L * L)
    def find_root(label,array):
        if label == array[label]:
            return array[label]
        else:
            array[label] = find_root(array[label],array)
            return array[label]
    
    #now for saving the position of the sites with the same label, i need a dictionary
    clusterL_position={}
    for i in range(count+2):
        clusterL_position[i]=[]
    
    
    
    for j in range(1,L+1):
        for i in range(1,L+1):
            #we look at a square grid and don't get out of bound
            #look for on sites
            if grid[i,j]!=0:
                
                #look for its left and top neighbor
                top_n=label_grid[i-1,j]
                left_n=label_grid[i,j-1]
                #now we have three ways
                
                if top_n==0 and left_n==0:
                    #new cluster
                    
                    label_grid[i,j]=label_counter
                    labels[label_counter] = label_counter
                    cluster_size[label_counter] += 1
                    clusterL_position[label_counter].append((i,j))
                    label_counter+=1
                    
                    
                elif top_n==0 and left_n!=0:
                    #link both to root
                    
                    label_grid[i,j-1]=find_root(left_n,labels)
                    label_grid[i,j]=find_root(left_n,labels)
                    clusterL_position[find_root(left_n,labels)].append((i,j))
                    cluster_size[find_root(left_n,labels)] += 1
                    

                elif top_n!=0 and left_n==0:
                    #link both to root
                    label_grid[i-1,j]=find_root(top_n,labels)
                    label_grid[i,j]=find_root(top_n,labels)
                    clusterL_position[find_root(top_n,labels)].append((i,j))
                    cluster_size[find_root(top_n,labels)] += 1
                    

                elif top_n!=0 and left_n!=0:
                    #compare labels
                    root_L=find_root(left_n,labels)
                    root_T=find_root(top_n,labels)
                    label_grid[i - 1][j] = root_T
                    label_grid[i,j - 1] = root_L
                    min_r=min(root_L,root_T)
                    max_r=max(root_L,root_T)
                    
                    label_grid[i,j] = min_r
                    clusterL_position[min_r].append((i,j))
                    if root_L==root_T:
                        cluster_size[root_L] +=1
                    
                    if root_L != root_T:
                        #unite roots
                        #join two clusters and ignore the top one
                        cluster_size[min_r] = cluster_size[min_r] + cluster_size[max_r] + 1
                        cluster_size[max_r]=0
                        labels[labels == max_r] = min_r
                        clusterL_position[min_r].extend(clusterL_position[max_r])
                        clusterL_position[max_r] = []
                        
                        
   
    for j in range(1,L+1): 
        for i in range(1,L+1):
            label_grid[i, j] = find_root(label_grid[i, j],labels)
            
    return label_grid, cluster_size, labels , clusterL_position
                    
                    
im, cluster_s ,label, clusterP=HK(Plane(10,0.4)) 
#print(clusterP)

def if_percolation(im,cluster_cor):
    first_column=im[:,1]
    last_column=im[:,-2]
    #print(last_column)
    for i in last_column:
        for j in first_column:
            if i==j and i!=0:
                #i dont want the inf cluster
                cluster_cor[i]=[]
                return 1 ,cluster_cor
    
    
    return 0, cluster_cor



#now i will take the second biggest cluster and its positions and calculate the RG
'''def find_biggest_key(cluster_cor):
    
    biggest_label = 0
    biggest_count = 0  
    for key, coor in cluster_cor.items(): 
        count = len(coor) 
        if count > biggest_count: 
            biggest_count = count 
            biggest_label = key 

    return cluster_cor[biggest_label] if cluster_cor else 0

print(im)
print("this is cluster_coordiante", clusterP)
#print(im[:-1,:-1])
print("hi")
print(if_percolation(im,clusterP))
#plt.imshow(im[:-1,:-1])  
#print(f'did we have percolation?{if_percolation(im)}')
#plt.title(f"this is for L={L} and p={p}")
plt.show()
print(cluster_s)
did, cluster_cord=if_percolation(im, clusterP)
print("second biggest cluster")
print(find_biggest_key(cluster_cord))'''



def gyration_r(cluster_cor):
    Rg_all=[]
    total_weight = 0
    weighted_sum = 0
    
    #Weights = [] 
    #look at each cluster separately
    for label, coor in cluster_cor.items():  # Number of points in this cluster
        #print(label, "this is label")
        #print("damn")
        #print(coor)
        #size
        S=len(coor)
        #print("len coor", S)
        if  S==0:
            continue
        #print(f"this is our coordiante for label={label}", coor)
            
        C_M_x, C_M_y = np.mean(coor, axis=0)
        #print("these are cm_x y", C_M_x, C_M_y)
        
        SumR=0

        # Iterate through all cluster points
        for i in range(S):
            x, y = coor[i]
            SumR += (x**2 - C_M_x**2)+ (y**2 - C_M_y**2)
            

        
        Rg = (SumR) / S
        Rg_all.append(np.sqrt(Rg))
        #print(Rg_all)
        #Weights.append(S)
        weighted_sum += Rg * S  
        total_weight += S 

        
   
    return weighted_sum/total_weight if Rg_all else 0
    




p_range = np.arange(0,1.05, 0.05)
L_range=[10,20,40,80,160]

for L in L_range:
    averag= []
    
    for p in p_range:
        #run this 100 time for each p
        #this is for L=10
        
        for i in range(100):
            sample_grid,cluster,_, cluster_co=HK(Plane(L,p))
            percolation, cluster_no_inf_coor=if_percolation(sample_grid, cluster_co)
            array.append(gyration_r(cluster_no_inf_coor))
            #array[np.isnan(array)] = 0
        averag.append(np.average(array))
        array = []  
         
             
    plt.plot(p_range,averag,  label= f"this is for L = {L}")
    plt.xlabel("probability")
    plt.ylabel("ksi")
    plt.legend()

plt.show()


'''
def Length(pcl, D, pcinf, nu):

    return (D * np.abs(pcl - pcinf)) ** (-nu)

# Data
L = np.array([10, 20, 40, 80, 160])  
pcl = np.array([0.517, 0.555, 0.572, 0.578, 0.580]) 

# Initial guesses 
p0 = (1, 0.6, 1.5)


bounds = ([0, max(pcl)+0.015, 1.4], [np.inf, 1, 2]) 




params, covariance = curve_fit(Length, pcl, L, p0=p0, bounds = bounds, maxfev=8000)
D, pcinf, nu = params
print("Optimized D:", D)
print("Optimized pcinf:", pcinf)
print("Optimized nu:", nu)

    
L_fitted = Length(pcl, D, pcinf, nu)


plt.figure(figsize=(8, 5))
plt.scatter(pcl, L, label="Data")
plt.plot(pcl, L_fitted, color='red',label="Fit")
plt.xlabel("pcl")
plt.ylabel("L")
plt.legend()
plt.show()
print("pcl:",pcl)
print('L',L)'''

'''
pcinf=0.595
log_pcl_pcinf=np.log(np.abs(pcl-pcinf))
log_L=np.log(L)
plt.scatter(log_L,log_pcl_pcinf)
plt.xlabel("logL")
plt.ylabel("log(pcl-pcinf)")
m  , b = np.polyfit (log_L ,log_pcl_pcinf , 1)
line=m*log_L+b
plt.plot(log_L, line)

plt.show()

m'''










