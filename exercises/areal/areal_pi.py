import numpy as np

N = 10

treff = [False] * N

for i in range(N):
    x = np.random.uniform(-1,1)
    y = np.random.uniform(-1,1)
    if not x**2 + y**2 > 1:
        treff[i] = True

print(treff)
print(treff.count(True))
print(treff.count(False))
