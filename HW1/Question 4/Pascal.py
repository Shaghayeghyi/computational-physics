import numpy as np
import math as m
import matplotlib.pyplot as plt

#at first we need to create the pascal triangle
#in the pascal triangle each number is a polynomial factor
#such that each number is (m,k) were m is the row and k is the position both starting from 0
#we also notice that each row like i has i+1 positions for numbers
# then n as the number of row is our arbitrary parameter
#we also has two loops
n=64
'''for i in range(n):
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
    print()'''
#i need to assign a pixel to each number
#a 2D pixel will need a 2D array and i can use imshow i assume :)
#i will assign 1 with white and 0 with black and just turn the odd numbers black
#we have n rows and in each row we have 2*n-1 positions, starting from 1 counting spaces and number to reach the other 1
pixel=np.ones((n, 2*n-1))
#at this point every number and spcae is white

for i in range(n):
    for j in range(i+1):
        number=m.factorial(i) // (m.factorial(j) * m.factorial(i - j))
        if number%2==1:
            #number is odd so it should get black(number 0)
            pixel[i,(n-i-1)+2*j]=0
            #consider the space between numbers too!
#now lets plot
plt.figure(figsize=(5, 5))
plt.imshow(pixel, cmap='gray', interpolation='none')
plt.show()
'''
#just checking
a=np.ones((3,4))
print(a)
a[2,3]=0
print(a)'''
