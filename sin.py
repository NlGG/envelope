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


fig, ax = plt.subplots()
x = np.linspace(0, 10, 200)

for n in range(-9, 10):
    y = n * np.sin(1/4 * x);
    ax.plot(x, y, 'r-', linewidth=2, label='$y=' + str(n) + '  * \sin(x)$')


ax.legend()
plt.show()