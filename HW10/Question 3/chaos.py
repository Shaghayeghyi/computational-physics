import numpy as np
import matplotlib.pyplot as plt

#values of r
rs= np.arange(0,1,0.002)
forget=10000
data=100

def chaos(forget,data,rs,x0):
    all_rs=[]
    xs=[]
    for r in rs:
        x = x0
        for i in range(forget):
            x=4*r*x*(1-x)
        for n in range(data):
            x=4*r*x*(1-x)
            xs.append(x)
            #all_rs.append(r)
        # i believe this is a faster version
        all_rs.extend(np.full(data, r))
    
    return xs, all_rs

X, R =chaos(forget,data,rs,0.5)
plt.figure(figsize=(12, 8))
plt.scatter(R, X, s=0.1)
plt.xlabel("r")
plt.ylabel("x")
plt.title("bifurcation")
plt.show()
 
    
    
