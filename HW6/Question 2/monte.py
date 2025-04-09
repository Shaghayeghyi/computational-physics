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
    start=time()
    for i in range(N):

        random_x=np.random.uniform(0,2)
        simple_y=np.exp(-random_x**2)
        sample.append(simple_y)
    #so we have our sample now we need to calculate the mean

    integral=2*np.mean(sample)
    #print(integral)
    
    stop=time()
    
    #for the error we need to calculate the std over sqrt(N)
    sample_error=np.std(sample)/np.sqrt(N)
    print(sample_error)

    #we should calculate the real error too

    real_error=real_result()-integral
    print(real_error)

    #let's see how much time it take

    duration=stop-start
    print(duration)

    

def important(N):

    sample=[]
    start=time()
    for i in range(N):
        #just chane the generator
        random_x=-np.log(np.random.uniform(np.exp(-2), 1))
        important_y=np.exp(-random_x**2)/np.exp(-random_x)
        sample.append(important_y)
    #so we have our sample now we need to calculate the mean

    integral=(1-np.exp(-2))*np.mean(sample)
    print(integral)
    
    stop=time()
    
    #for the error we need to calculate the std over sqrt(N)
    sample_error=np.std(sample)/np.sqrt(N)
    print(sample_error)

    #we should calculate the real error too

    real_error=real_result()-integral
    print(real_error)

    #let's see how much time it take

    duration=stop-start
    print(duration)
    
important(10000)
