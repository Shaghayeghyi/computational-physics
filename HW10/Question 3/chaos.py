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
X = np.array(X)
R = np.array(R)
plt.figure(figsize=(12, 8))
plt.scatter(R, X, s=0.1)
plt.xlabel("r")
plt.ylabel("x")
plt.title("bifurcation")
plt.show()


#now we need to find the place and width of bifurcation
r_list=[]
x_list=[]
for r in np.unique(R):
    x_r = X[R == r]
    r_list.append(r)
    x_list.append(x_r)

#just checking :)
#print(r_list)
#print(x_list)

r_n = []
#we start by one branch
current_count = 1

for i in range(len(r_list)):
    r = r_list[i]
    x_r = x_list[i]
    unique_x = np.unique(np.round(x_r,4))
    count = len(unique_x)
    #count has doubled
    if count == 2 * current_count:
        r_n.append(r)
        current_count = count
    elif count > current_count:
        current_count = count


print("bifurcation at:")
print(np.round(r_n, 5))
    
    
 
#alpha



    
    
    

