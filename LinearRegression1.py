#!/usr/bin/python
#coding:utf-8

import numpy as np
from scipy.optimize import curve_fit
import pylab as pl


# Creating a function to model and create data
def func(x, a, b):
    return a * x + b
# Generating clean data
x = np.linspace(0, 10, 100)
y = func(x, 1, 2)
# Adding noise to the data
yn = y + 0.9 * np.random.normal(size=len(x))
# Executing curve_fit on noisy data
popt, pcov = curve_fit(func, x, yn)
# popt returns the best fit values for parameters of
# the given model (func).

print(popt)
a1 , b1 = popt
y1 = func(x, a1, b1)

pl.plot(x, y1, label=u"拟合结果")
pl.plot(x, y, label=u"真实数据")
pl.plot(x, yn, label=u"带噪声的实验数据")
# pl.plot(x, func(x, plsq[0]), label=u"拟合数据")




pl.legend()
pl.show()
