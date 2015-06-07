#!/usr/bin/python
#-*- encoding: utf-8 -*-
# Quantitative Economics Web: http://quant-econ.net/py/index.html
# 尾山ゼミwiki: http://oyamazemi.wiki.fc2.com/

from __future__ import division
import math
import functools  #for python3
from random import uniform, normalvariate
import matplotlib.pyplot as plt
import numpy as np

def envelope(expression):
    fig, ax = plt.subplots()
    y = np.arange(0, 100, 0.5)

    colormap = ['b', 'c', 'g', 'y', 'm', 'r', 'k']

    for k in range(1, 101, 1):
        color = colormap[k % 6]
        k = k / 10.0
        c = expression(y, k)
        
        min_index = c.argmin()
        left_bound = max(min_index - 8, 0)
        right_bound = min(min_index + 8 + 1, 200 - 1)
        y2 = y[left_bound : right_bound]
        c2 = c[left_bound : right_bound]
        ax.plot(y, c, color=color, linewidth=1)

    ax.plot(0, 0, color='c', linewidth=1 ,label="Short-Run Cost Curves")

    plt.xlim(0, 30)
    plt.ylim(0, 100)
    plt.title('Long-Run Cost Curve')
    plt.xlabel('Y: Production')
    plt.ylabel('C: Total Cost')
    plt.legend()
    plt.suptitle('simulation and execution result')
    plt.show()


envelope(lambda y, k: 1/3 * 1/50*((1/2*y-2*k**3) ** 3+(2*k**3)**3) + 1/2 * 1/5*k*((1/2*y-(5*k**3-5*k**2+k))**2-(5*k**3-5*k**2+k) **2) + 1 * 1/4 * 1/k * y + 1/100*4*k**6*y + (5*k**3-5*k**2+k) + 1/3*(k-2)**3+5*k+5)
#envelope(lambda y, k: 1/8 * (y - 10 * k) ** 2 + 1/3 * k ** 2 - 2 * k + 4)
#envelope(lambda y, k:1/16  * ((1/2*y-2*k**3) ** 3 + (2*k**3)**3) +1/300*5*k*((1/2*y-(8*k**3-5*k**2+5))**2-(8*k**3-5*k**2+5) **2)+5*k)


