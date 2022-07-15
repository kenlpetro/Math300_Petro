# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:09:00 2022

@author: rocko
"""

def trapezoid(f,a=0,b=1,n=100):
    if n<=0:
        raise ValueError('n must be positive',n)
    h=(b-a)/n   #length of each slice
    total=0     #holds values of the sum
    
    for i in range(1,n):
        total += f(a+h*i)
    
    return (h/2)*(f(a)+f(b)+2*total)

def f(x):
    return x*x*x

a=trapezoid(lambda x:x*x*x,a=10,b=100,n=1000)