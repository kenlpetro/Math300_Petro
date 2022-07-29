def summ (N=100):
    total=0
    for n in range(1,N+1):
        total+=1/(n*n)
    return total
summ()