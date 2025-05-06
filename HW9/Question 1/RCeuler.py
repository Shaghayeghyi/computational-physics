import numpy as np
import matplotlib.pyplot as plt
from time import time


def euler(h,q,step):
    time=np.arange(int(step))
    qs=[]
    qs.append(q)
    for i in time:
        q=q+h*(1-q)
        qs.append(q)
        
        

        
    



#define the real answer
def real_result(t):

    return 1-np.exp(-1*t)

