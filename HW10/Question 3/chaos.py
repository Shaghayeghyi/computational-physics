import numpy as np
import matplotlib.pyplot as plt

#values of r
rs= np.arange(0,1,0.0001)
forget=1000
data=200

def chaos(forget,data,r,x0):
    x=x0
    for i in range(forget):
        x=4*r*x*(1-x)
    xs=[x]
    for n in range(data):
        x=4*r*x*(1-x)
        xs.append(x)
    return xs
    


    
    
    
