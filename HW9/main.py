import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt


# User Defined Variables
Initial_Guess = 4
# Define the function to be minimized
def Func(x):
    return (x-2)**2 + np.sin(5*x)
    #return np.sin(x) * (1 + np.cos(2*x))

# Plot the function
x = np.linspace(-5, 5, 100)
y = Func(x)

# Use the minimize function to find the minimum
result = minimize(Func, x0=Initial_Guess, method ='Nelder-Mead')
print(result)

# Plot the minimum
plt.plot(x, y)
plt.scatter(result.x, result.fun, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Minimized Function')
plt.fill_between([-2,4], 0,[20,20] , color='blue', alpha=.2, label='Sometimes Inaccurate Optimization')
plt.text(0.5, 0.5, r'$f(x)= (x-2)^2 + \sin(5x)$', fontsize=12, transform=plt.gca().transAxes)
plt.legend()
plt.savefig("Optimization.png")
plt.show()

