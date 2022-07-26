import random
import matplotlib.pyplot as plt
import Circle

circles=[Circle.circle() for i in range(50)]

for c in circles:
    c.cx=random.uniform(-40,40)
    c.cy=random.uniform(-40,40)
    c.r=random.uniform(0,10)
    

figure, ax=plt.subplots()
ax.axis([-50,50, -50,50])
circle_plots=[None]*50


for i in range(len(circle_plots)):
    r=random.random()
    g=random.random()
    b=random.random()
    color=(r,g,b)
    circle_plots[i] = plt.Circle((circles[i].cx,circles[i].cy),
                                 circles[i].r,fill=True,color=color)
    ax.add_artist(circle_plots[i])
    
plt.show()