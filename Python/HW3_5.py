import sympy as sp
x = sp.Symbol('x')

f = (x**3)-(((sp.cos(sp.pi*x))**2)/(((2*x)**2)+1))+((11/3)*(x**2))-1

diff_f=f.diff(x)
print(diff_f)