import numpy as np
import matplotlib.pyplot as plt
from random import randint

#central limit theorem
def central_limit(N):
    runs = 100000
    G_data =[]
    for run in range(runs):
        #use built in functions
        #gaussian variable
        y =np.sum(np.random.randint(10, size=N))/N
        G_data.append(y)
    return G_data
Ns=[5]
for N in Ns:
    ys=central_limit(N)
    plt.hist(ys, bins=50 ,alpha=0.7, rwidth=0.85 , density=True)
    plt.xlabel("Average Value")
    plt.ylabel("Probability Density")
    plt.title(f'Distribution of sum of {N} Variables')
    plt.show()
