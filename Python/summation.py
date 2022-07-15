# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 11:04:08 2022

@author: rocko
"""

def summ (N=100):
    total=0
    for n in range(1,N+1):
        total+=1/(n*n)
    return total
