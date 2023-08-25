import numpy as np
import matplotlib.pyplot as plt

# vi skal se på numerical error i punktet x=0
# delta x, altså arrayen dx, er når vi deler det opp i mindre og mindre biter

# lag vektor med 10-16, 10-15.....10-1 (delta x verdier)
# regn ut numerisk error

# create log spaced numbers from 10**-16 to 10**-1
dx = np.logspace(-16, -1, 16)
print(dx)

# array med e**deltaX
# np.exp(array) gir ny array med e opphøyd i det fra array
e_raisedTo_dx = np.exp(dx)

numericalSolution = np.abs((e_raisedTo_dx - 1)/dx-1)
plt.plot(dx,numericalSolution)

plt.xscale('log') 
plt.yscale('log')
plt.show()
