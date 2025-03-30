import numpy as np
import matplotlib.pyplot as plt
from random import randint,random

#let's look at python's RNG

def generator(N):
    
    number_array=np.zeros(10)
    for num in range(N):
        random_number = randint(0,9)
        #insert it to the array
        number_array[random_number]+=1

    return number_array

print(generator(100))
