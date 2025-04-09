import numpy as np
import matplotlib.pyplot as plt
import random
from time import time

#we want to calculate simple and important integral

def real_result():

    def f_x(x):
        return np.exp(-x**2)
    
    answer , error = quad(f_x, 0, 2)

    return answer

#what is the real output
result=real_result()
#print(result)

def simple(N):

    sample=[]

    for i in range(N):

        random_x=np.random.uniform(0,2)
        simple_y=np.exp(-random_x**2)
        sample.append(simple_y)
    #so we have our sample now we need to calculate the mean

    integral=2*np.mean(sample)
    #print(integral)

    #for the error we need to calculate the std over sqrt(N)
    sample_error=np.std(sample)/np.sqrt(N)
    print(sample_error)

    

simple(1000)
