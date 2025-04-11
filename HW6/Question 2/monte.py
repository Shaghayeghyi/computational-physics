import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.integrate import quad
from time import time
import pandas as pd

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
    sample_error=2*np.std(sample)/np.sqrt(N)
    #print(sample_error)

    #we should calculate the real error too

    real_error=np.abs(real_result()-integral)
    #print(real_error)

    #let's see how much time it take

    duration=stop-start
    #print(duration)
    return integral , sample_error , real_error , duration
    

def important(N):

    sample=[]
    start=time()
    for i in range(N):
        #just chane the generator
        random_x=-np.log(np.random.uniform(np.exp(-2), 1))
        important_y=np.exp(-random_x**2)/np.exp(-random_x)
        sample.append(important_y)
    #so we have our sample now we need to calculate the mean
    #the result has a new formula
    integral=(1-np.exp(-2))*np.mean(sample)
    #print(integral)
    
    stop=time()
    
    #for the error we need to calculate the std over sqrt(N)
    sample_error=(1-np.exp(-2))*np.std(sample)/np.sqrt(N)
    #print(sample_error)

    #we should calculate the real error too

    real_error=np.abs(real_result()-integral)
    #print(real_error)

    #let's see how much time it take

    duration=stop-start
    #print(duration)
    return integral , sample_error , real_error , duration
    
#data frame for comparing
def table(Ns):
    results = []
    
    real_value = real_result()
    #let's create two arrays to save the important and simple errors
    error_im=[]
    error_si=[]
    for N in Ns:
        #simple variables
        s_integral, s_samp_err, s_real_err, s_time = simple(N)
        error_si.append(s_samp_err)
        #important variables
        i_integral, i_samp_err, i_real_err, i_time = important(N)
        error_im.append(i_samp_err)
        # add a row
        results.append({
            'N': N, 'real value': real_value,'simple integral': s_integral,'simple sample error': s_samp_err,'simple difference error': s_real_err,'simple time': s_time,
            'important integral': i_integral,'important sample error': i_samp_err,'important difference error': i_real_err,'important time': i_time})
   
    df = pd.DataFrame(results)
    return df , error_im , error_si

N_values = [100, 1000, 10000, 100000, 1000000]
results_df, important_E,simple_E = table(N_values)


print(results_df)



#plots
plt.plot(N_values, important_E, label="important")
plt.plot(N_values, simple_E, label="simple")
plt.xlabel("N")
plt.ylabel("error")
plt.legend()
plt.show()
