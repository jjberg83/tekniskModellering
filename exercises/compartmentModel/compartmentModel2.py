import numpy as np
import scipy as sp
from scipy import integrate
import matplotlib.pyplot as plt

def SIRt_model(t, *, beta, tau, N=1000, I0=1, R0=0):
    
    def rhs(X,t):
        S, I, R = X
        return [-beta*S*I/N, +beta*S*I/N - I/tau, +I/tau]
    
    X0 = [N-I0-R0, I0, R0]
    sol = integrate.odeint(rhs, X0, t)
    return sol

X0 = np.array([S0, I0, R0])
tf = 200; t = np.linspace(0, tf, 1000)
sol = SIRt_model(t, beta=0.06, tau, N=1000, I0=1, R0=0)
plt.plot(t, sol[:,0], label='S')
plt.plot(t, sol[:,1], label='I')
plt.plot(t, sol[:,2], label='R')
plt.legend()