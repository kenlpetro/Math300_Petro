import matplotlib.pyplot as plt

def Q3 (N,x=[]):
    
    x_totals=[]
    for i in range(len(x)):
        total=0
        for n in range(1,N+1):
            total+=((x[i]**(n))/n)
        
        x_totals.append(total)
        return x_totals
    plt.plot(x,x_totals)