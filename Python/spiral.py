import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

fig=plt.figure()
ax=plt.axes(xlim=(-50,50),ylim=(-50,50))
line,=ax.plot([],[],lw=2)

def func():
    line=ax.set_data([],[])
    return line,


xarray=[]
yarray=[]

def animate(i):
    t=.1*i
    x=t*np.sin(t)
    y=t*np.cos(t)
    xarray.append(x)
    yarray.append(y)
    line.set_data(xarray,yarray)
    return line,

anim=animation.FuncAnimation(fig,animate,frames=500,interval=20)
plt.show()