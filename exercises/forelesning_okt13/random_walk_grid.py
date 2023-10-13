#%%
import numpy as np
import matplotlib.pyplot as plt

# Foreleser legger også hele denne koden ut


# Globale variabler ender med underscore
global Walkers_
HUMAN_ = 0
ZOMBIE_ = 1
N_ = 10 # population size
I_ = 1 # people initially infected
nx_ = 10 # lengde på grid i X retning
ny_ = 10 # lengde på grid i Y retning
STATE_ = np.repeat(HUMAN_, N_)
STATE_[0] = ZOMBIE_
q_ = 0.9 # sjanse for å bli smittet ved treff mellom to personer
Walkers_ = np.random.randint(0,[nx_, ny_], size=(N_,2))
Walkers_old_ = np.copy(Walkers_)

H_=Walkers_[STATE_==HUMAN_]
Z_=Walkers_[STATE_==ZOMBIE_]
plt.scatter(H_[:,0],H_[:,1],c='b',s=120)
plt.scatter(Z_[:,0],Z_[:,1],c='g',s=60) #60 gjør at prikk er mindre
plt.grid()
plt.show()

def plot_walkers():
    plt.close()
    H_=Walkers_[STATE_==HUMAN_]
    Z_=Walkers_[STATE_==ZOMBIE_]
    plt.xlim(0,nx_)
    plt.ylim(0,ny_)
    plt.scatter(H_[:,0],H_[:,1],c='b',s=120)
    plt.scatter(Z_[:,0],Z_[:,1],c='g',s=60)
    plt.grid()
    plt.show()

def move_walkers():
    global Walkers_
    u = np.array([[0,1],[0,-1],[1,0],[-1,0]]) # Retninger
    dir = np.random.randint(0,4,size=N_)
    Walkers_=Walkers_+u[dir] 

def check_illegal_move():
    wrong_place_x = np.logical_or(Walkers_[:,0]<0, Walkers_[:,0]>nx_)
    wrong_place_y = np.logical_or(Walkers_[:,1]<0, Walkers_[:,1]>ny_)
    return np.logical_or(wrong_place_x, wrong_place_y)

#step 1: init
Walkers_old_=np.copy(Walkers_)
plot_walkers()
#check_illegal_move()

#step 2: move
for i in range(20):
    move_walkers()
    idx=check_illegal_move()
    Walkers_[idx]=Walkers_old_[idx]
    Walkers_old_ = np.copy(Walkers_)
    plot_walkers()

#%%
u = np.array([[0,1],[0,-1],[1,0],[-1,0]]) # Mulige retninger
dir = np.random.randint(0,4,size=N_) 

# u[dir] gir en array med tilfeldig N trekninger av valgene i u
#%%