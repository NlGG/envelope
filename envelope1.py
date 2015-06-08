from __future__ import division
import math
import functools  #for python3
from random import uniform, normalvariate
import matplotlib.pyplot as plt
import numpy as np

def envelop():
    fig, ax = plt.subplots()
    y = np.linspace(0, 100, 100)
    colormap = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for k in range(1, 200, 1):
        color = colormap[k % 6]
        k = k / 10.0
        c3 = (1/5*y-k**3)**3+(k**3)**3
        c2 = 1/10*((1/5*y-k**3)**2-(k**3) **2)
        c1 = 1/10*k**3*y
        c0 = (k-3)**3 +5*(-1)**10*k + 27
        plt.xlim(0, 50)
        plt.ylim(0, 100)

        ax.plot(y, (c3+c2+c1+c0), color='c', linewidth=1)
        
    #c = 2 * math.sqrt(6) / 3 * y
    #ax.plot(y, c, 'b-', linewidth=2, label='$k = ' + str(k) + '$')

    #ax.legend()
    
    plt.show()


envelop()
