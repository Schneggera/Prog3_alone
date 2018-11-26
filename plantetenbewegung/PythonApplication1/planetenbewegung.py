
from math import fabs as abs
from math import sqrt 
import matplotlib.pyplot as plt
import numpy as np
speed_earth = (0, 29780)
mass_sun = 1.989 * 10**30
mass_earth = 5.972 * 10**24
pos_sun = (0, 0)
pos_earth = (147099760000, 0)
G = 6.672 * 10**-11
delta_T = 86400


def calc_grav_force(m1, m2, x1, x2, pos):
    x = sqrt((x2[0]-x1[0])**2 +(x2[1]-x1[1])**2)
    return (G*(m1*m2)/(abs(x)**3)*(pos/x))/m1

def calc_pos (t, delta_T, a, x, v):
    return (x + delta_T*v + (delta_T**2/2)*a)

def calc_speed (v, a, t):
    return v + a*t  

def plot(m1, m2, pos, x2, t, delta_T, v):
    i = 0
    lx = ly = []
    vx = v[0]
    vy = v[1]
    while i < 365:
        ax = calc_grav_force(m1, m2, pos, x2, pos[0])
        ay = calc_grav_force(m1, m2, pos, x2, pos[1])
        posx = calc_pos(t, delta_T, ax, pos[0], vx)
        posy = calc_pos(t, delta_T, ay, pos[1], vy)
        pos = (posx, posy)
        vx = calc_speed(vx, ax, t)
        vy = calc_speed(vy, ay, t) 
        lx.append(posx)
        ly.append(posy)
        t += delta_T
        i+=1 
    lxnp = np.array(lx)
    lynp = np.array(ly)
    plt.plot(lxnp, lynp)
    plt.show()  

plot(mass_earth, mass_sun, pos_earth, pos_sun, 0, delta_T, speed_earth)