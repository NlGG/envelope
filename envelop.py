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

def envelop():
    fig, ax = plt.subplots()
    y = np.linspace(0, 100, 100)
    colormap = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for k in range(1, 200, 1):
        color = colormap[k % 6]
        k = k / 10.0
        c = 1/8 * (y - 10 * k) ** 2 + k ** 2 - 2 * k + 4

        plt.xlim(0, y.max() * 1.1)
        plt.ylim(0, 30)

        ax.plot(y, c, color='c', linewidth=1)

    #c = 2 * math.sqrt(6) / 3 * y
    #ax.plot(y, c, 'b-', linewidth=2, label='$k = ' + str(k) + '$')

    #ax.legend()

    plt.show()


envelop()