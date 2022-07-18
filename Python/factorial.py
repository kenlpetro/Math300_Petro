import math
import matplotlib.pyplot as plt

def fact (N,x=[]):
    
    x_totals=[]
    for i in range(len(x)):
        total=0
        for n in range(N+1):
            total+=((-1)**N)*(x[i]**(2*n))/(math.factorial(2*n))
        
        x_totals.append(total)
        return x_totals
    plt.plot(x,x_totals)    