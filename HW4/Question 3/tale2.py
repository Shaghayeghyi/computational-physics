import numpy as np
import matplotlib.pyplot as plt
from random import randint,random

starting_positions=np.range(0,21)

probability_array=np.zeros(21)

probability_array[starting_position]=1

p=0.8
q=1-p

p_out=0.01

while sum(probability_array)>p_out:
    
    for j in len(probability_array):
        
        if probability_array[j]!=0:

            if j==20: #left
                probability_array[j-1]=q*probability_array[j]
            elif j==0: #right
                probability_array[j+1]=p*probability_array[j]           
            
            else:
                probability_array[j+1]=p*probability_array[j]
                probability_array[j-1]=q*probability_array[j]
        probability_array[j]=0 #moved out
                
