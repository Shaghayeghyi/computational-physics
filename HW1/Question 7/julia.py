import numpy as np
import matplotlib.pyplot as plt
import random
import math as m

#for the julia set we need to work with complex numbers
#we have a boundary with lenght r. we choose a random number
#we apply a function f(z) on it till it either gets out of boundary or we just reach the max iteration
#we save the number of iteration done for each random number and assigne a color to each

#i want to create a random number between 0 and 10


x=random.uniform(0,10)
y=random.uniform(0,10)
Ncomplex=complex(x,y)
print(Ncomplex)
