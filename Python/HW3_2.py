import matplotlib.pyplot as plt

def Q2 (N=10000):
    total=0
    for n in range(1,N+1):
        total+=(-1**(n+1))*(1/n)
        plt.plot(N,total)