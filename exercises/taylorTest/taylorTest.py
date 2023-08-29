#%%
import math
import matplotlib.pyplot as plt



# LISTE fremgangsmåten

#%%
# Denne funker ikke fordi for looper ikke godtar floats
# som denne inkrementerer med
# syntaks:
# for i in range(start, stop, steg):
x = []
sin = []
x_i = -math.pi
dx = (-x_i)/12

for i in range(x_i, -x_i, dx):
    x.append[x_i]
    sin.append(math.sin(x_i))
    x_i += dx

plt.plot(x,sin)
plt.show()

# %%
#%%
# shift + enter for å kjøre denne og hoppe til neste blokk
# Denne funker ikke fordi for looper ikke godtar floats
# som denne inkrementerer med
# syntaks:
# for i in range(start, stop, steg):
x = []
sin = []
x_i = -math.pi
dx = (-x_i)/12

for i in range(x_i, -x_i, dx):
    x.append[x_i]
    sin.append(math.sin(x_i))
    x_i += dx

plt.plot(x, sin)
plt.show()
