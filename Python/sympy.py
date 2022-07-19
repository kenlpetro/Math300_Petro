import sympy as sp
import numpy as np
from IPython.display import display


a=sp.pi
b=np.pi

x,y,a,b,c=sp.symbols('x,y,a,b,c')
#sp.var('u,y')
#display(x+x-y)

'''
expr=(x+y)**4
display(expr.expand())

display(newexpr.subs(u,2))
display(newexpr.subs(u,2).factor())
'''

'''
expr=1/((x+1)*(x-3))
display(expr.apart())
display(expr.together())
display(sp.diff(x**4,x,3))
display(sp.integrate(1/x,(x,1,3)))
display(sp.integrate(1/x,(x,1,sp.oo)))
display(sp.solve(x**2+1))
display(sp.solve((a*x**2+b*x+c),x))
'''