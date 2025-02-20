import numpy as np
import math as m
import matplotlib.pyplot as plt

#at first we need to create the pascal triangle
#in the pascal triangle each number is a polynomial factor
#such that each number is (n,k) were n is the row and k is the position both starting from 0
#we also notice that each row like i has i+1 positions for numbers
# then n as the number of row is our arbitrary parameter
#we also has two loops
n=128
for i in range(n):
    #we need spacing from left, like a half empty square
    print((n-i)*" ", end=" ")
    #we also stop the automatic line change
    for j in range(i+1):
        #at row i and position j
        #we have n rows and i+1 number on each row
        number=m.factorial(i) // (m.factorial(j) * m.factorial(i - j))
        if number%2==0:
            print("□", end=" ")
        else:
            print("■",end=" ")
    print()
