#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

#%%
alfa = 10
x = np.linspace(0, 10)

def linear(x):
    return 3 + 2*x + alfa * np.random.random(len(x))


plt.scatter(x, linear(x))
plt.show()

# %%
# Create data frame
df = pd.DataFrame({'x': x, 'y': linear(x)})
df.info()

# %%
#df.head()
# %%
#df.tail()
# %%
#df.tail(10)
# %%
df.describe()
# %%
#her eksporterer vi fil til excel
df.to_excel('Example2.xlsx', index=False)
# %%
# her leser vi den inn igjen
df1 = pd.read_excel('Example2.xlsx')
# %%
# Vi åpner filen i Excel
# La alfa = 0 (altså ingen noise)
# Marker hele 70 % av tabellen
# Recommended Charts (velg den øverste)
# Gå inn i innstillinger og velg "Display equation on chart" og "Display R**2"
# %%
# Gjør det samme som over, men la alfa = 10

# %%
# lager en ny kolonne, der han finner y verdiene fra modellen
# ved å legge inn formelen i cellen øverst
# sett inn = 2* (trykk på x cellen i første linje) + 3
# trykk Enter
# trekk i Grønn boks nedover for hele kolonnen
# I eksempel 1, blir denne kolonnen identisk med faktisk y
# siden vi ikke har noise