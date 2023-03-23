import numpy as np
#from Random import Random

def coin_flips(p, N):
    """ Simulate N coin flips with a biased coin with probability of heads p """
    flips = np.random.binomial(1, p, N)  # 1 represents heads, 0 represents tails
    return np.sum(flips)  # return the number of heads


import matplotlib.pyplot as plt

true_p_values = np.linspace(0,1, 101)  # 101 evenly spaced true values of p from 0 to 1
measured_p_values = [] # initialize an array to store the measured values
true = []
for i in true_p_values:
    for j in range(1000):
        d = coin_flips(i,10)
        measured_p_values.append(d)
        true.append(i)
    
plt.hist2d(true, measured_p_values)
plt.xlabel("True p")
plt.ylabel("Measured p")
plt.show()
