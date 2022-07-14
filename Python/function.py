# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:09:00 2022

@author: rocko
"""

import numpy as np

def trapezoid(f,a=0,b=1,n=100):
    if n<=0:
        raise ValueError('n must be positive',n)

h=(b-a)/n
for k in range(1),
    s=s+h