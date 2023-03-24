import numpy as np
from Random import Random
import matplotlib.pyplot as plt

#Changing parameters
seed = 5555
N_Coin = 10 # Number of Coins/Measurements
Nexp = 1000 # Number of Experiments



true_p_values = np.linspace(0,1, 101)  # 101 evenly spaced true values of p from 0 to 1
measured_p_values = [] # initialize an array to store the measured values
true = [] #Store the repeated true values

Coins = Random(seed)


for i in true_p_values:
    for j in range(Nexp):
        d = Coins.Binomial(N_Coin, i)
        measured_p_values.append(d)
        true.append(i)
    
plt.hist2d(true, measured_p_values)
plt.xlabel("True p")
plt.ylabel("Measured p")
plt.savefig("Construction")
