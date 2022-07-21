import numpy as np

A=np.mat('1 2;3 4')
b=np.mat('5;8')

x=np.linalg.solve(A,b)
print(x)