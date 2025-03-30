import numpy as np
import matplotlib.pyplot as plt
from random import randint,random

#central limit theorem
def central_limit(N):
    
    runs=10000
    #create gaussian variables
    for run in range(runs):
        G_data=[]
        gaussian_var=0
        
        for n in range(N):
            random_number=randint(0,9)
            gaussian_var+=random_number
            
        G_data.append(gaussian_var)

    return G_data



    
