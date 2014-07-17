#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

How to raise a float to a certain power in Python?

¿Cómo elevar un número float a una potencia en Python?
'''

#create a float number
f = 3.3
print(f)

#the ** operator raises a number to a power
f_pow = f ** 3
print(f_pow)

#raises 'f' to a negative power
f_pow = f ** -2.6
print(f_pow)

import math

#the pow() method raises the first argument to the power defined in the
#second argument.
f_pow = math.pow(f, 3)
print(f_pow)
