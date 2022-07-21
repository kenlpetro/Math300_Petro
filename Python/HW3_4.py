import matplotlib.pyplot as plt
import numpy as np
"""
def midpoint(f,a,b,n):
    h=(b-a)/n
    while (a<b):
        x=(a+a+h)/2
  """      
def midpoint(f,a=0,b=1,n=10):
    h=(b-a)/float(n)
    x=np.linspace(a,b,h) #most likely what is causing problems
    l=0
    for i in range (1,len(x)):
        l+=f((x(i)+x(i+1))/float(2))
    l*=h

    z=np.arange(a,b+l,l)
    plt.plot(z,f(x))
     
    mid=np.arange(a,b,h)
    plt.bar(mid, f(mid), align='midpoint')
    plt.xlim(a,b)
    plt.show()

def f(x):
    return x*x