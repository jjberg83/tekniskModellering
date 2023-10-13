#%%
import numpy as np
import scipy as sp
from scipy import integrate
import matplotlib.pyplot as plt

beta = 0.06
N = 1000
I0 = 1
S0 = N - I0

def rhs(X, t):
    S, I = X
    return [-beta*S*I/N, +beta*S*I/N]

X0 = np.array([S0, I0])
tf = 200; t = np.linspace(0, tf, 1000)
sol = integrate.odeint(rhs, X0, t)

plt.plot(t, sol[:,0], label = 'S')
plt.plot(t, sol[:,1], label = 'I')
plt.legend()

# cond install scipy
#sp.integrate.odeint()
# %%
