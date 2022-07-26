import matplotlib.pyplot as plt
import numpy as np

'''
def riemann (f,a=0,b=1,n=10):
    l=np.linspace(a,b,n)
    plt.plot(l,f(l))
    plt.bar(l,f(l))    
def f(x):
    return x*x
'''


def riemannplot(f,a=0,b=1,n=10):
    l=(b-a)/1000
    l_2=(b-a)/n
    x=np.arange(a,b+l,l)
    plt.plot(x,f(x))
    
    riemannx=np.arange(a,b,l_2)
    plt.bar(riemannx, f(riemannx),align='edge', width=l_2)
    plt.xlim(a,b)
    plt.show()

def f(x):
    return x*x
