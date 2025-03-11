import numpy as np
import matplotlib.pyplot as plt
from random import random,randint
#we want to look at pecolation using HK algorithm
#we have a top left check system so we will get rid of on row and column
#we need an array so save the size of clusters
#we need a plane LxL
#we should create a function that leads us to the root:)
L=10
p=0.3

def Plane(L,p):
    plane = np.zeros((L,L+2),dtype = int)#L+2 for side's column
    plane[:,0]=1
    plane[:,-1]=100
    count=0
    k=3
    for j in range(1,L):
        for i in range(1,L):
            random_p=random()
            if random_p<p:
                plane[i,j]=1
            #if the site is on
            if plane[i,j]!=0:
                left_n=plane[i,j-1]
                top_n=plane[i-1,j]
                #if none of them are on
                if top_n==0 and left_n==0:
                    #we need a new number
                    plane[i,j]=k
                    #the size of cluster with number k increases
                    cluster_size[k]=1
                    k=k+1
                if top_n!=0 and left_n==0:
                    plane[i,j]=top_n
                    cluster_size[top_n]+=1
                if top_n==0 and left_n!=0:
                    plane[i,j]=left_n
                    cluster_size[left_n]+=1
                else:
                    label=max(top_n, left_n)
                    plane[i,j]=label
                    
                    
                    
                    
            
