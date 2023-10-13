#%%
import numpy as np
# import scipy as sp
# from scipy import integrate
import matplotlib.pyplot as plt

S = 1000
I = 1
tStart = 0
tEnd = 1000
deltaT = 1
beta = 0.06
N = 1000
I = 1
sol_S = [S]
sol_I = [I]
sol_T = [x * deltaT for x in range(tStart, int((tStart+tEnd)/deltaT))]


while (tStart <= tEnd):
    P = (deltaT*beta*sol_I[-1])/N
    for i in range(sol_S[-1]):
        x = np.random.uniform(0,1)

        if x < P:
            S -= 1
            I += 1
    sol_S.append(S)
    sol_I.append(I)
    tStart += deltaT

# print(f'Etter simulering er antall som kan bli smittet: {S}, og antall infiserte {I}')
plt.plot(sol_T, sol_S[:-2])
plt.plot(sol_T, sol_I[:-2])
plt.show()
# %%
