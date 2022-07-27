import random
import math
import matplotlib.pyplot as plt
class animal():
    def __init__(self,x=0,y=0):
        self.hitpoints=100
        self.x=x
        self.y=y
        
    def move(self,x_min,x_max,y_min,y_max):
        a=random.randint(1,4)
        
        if a==1:
            self.y+=1
        elif a==2:
            self.x+=1
        elif a==3:
            self.y-=1
        elif a==4:
            self.x-=1
            
        if self.x <= x_min:
            self.x = x_min
        if self.x >= x_max:
            self.x = x_max
        if self.y <= y_min:
            self.y = y_min
        if self.y >= y_max:
            self.y = y_max
        
class predator(animal):
    pass
    def attack(self,animal):
        distance=math.sqrt((self.x - animal.x)**2 + (self.y - animal.y)**2)
        if distance<1:
            animal.hitpoint-=10
class prey(animal):
    pass
"""            
    def display(self):
        plt.plot(self.x,self.y,'o')
        plt.show()
"""