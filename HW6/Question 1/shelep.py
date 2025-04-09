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

