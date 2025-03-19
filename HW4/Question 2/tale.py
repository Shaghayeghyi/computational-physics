import numpy as np
import matplotlib.pyplot as plt
from random import randint,random

#define tale

def tale(p,position):
    start=position
    death_time=0
    x=start

    while -10<x<10:

        rand=random()

        if rand<p:
            x=x+1
            death_time=death_time+1
        else:
            x=x-1
            death_time=death_time+1
    return death_time
