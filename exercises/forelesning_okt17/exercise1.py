import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

init_velocity = 100 # vektor i både y og x retning
angle = 45*3.14/180
# angle = np.deg2rad(45) 
g = 9.81 # gir 50 tider (sjekk med print(len(t)))
T=(2*init_velocity*np.sin(angle))/g # Total time of flight
t = np.linspace(start= 0, stop = T)

def projectile(t):
    return (init_velocity*np.sin(angle)*t) - (0.5*g*(t**2)) 

df = pd.DataFrame({'t': t, 'y':projectile(t)})
df.to_excel('flight.xlsx', index=False)
yEne = projectile(t)

print()
plt.plot(t, yEne)
plt.show()

