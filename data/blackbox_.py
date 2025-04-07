#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 20:20:51 2025

@author: ajaome
"""

import numpy as np

def f(x):
    if x>37:
        f = -15.4 * np.log(x-35) +163.15493533
    else:
        #global max (28, 392)
        #local max (12, 360)
        f =  -((0.25*x - 3)**2 * (0.25*x - 5.) * (0.25*x - 8.) - 360)
    return f