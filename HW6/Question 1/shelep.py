import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import random

#with a basic analogy with the pool example, we will calculate the given integral


def real_result():

    def f_x(x):
        return x**3 - 5*x
    
    answer , error = quad(f_x, 0, 2)

    return answer

#what is the real output
result=real_result()


#approximation of min and max of function for correct boundary

def min_max():
    x_vals = np.linspace(0, 2, 1000)  # 1000 points in [0, 2]
    y_vals = x_vals**3 - 5*x_vals

    return np.min(y_vals) , np.max(y_vals)


