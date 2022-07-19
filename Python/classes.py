import random as rnd
class circle():
    def __init__(self, cx=0, cy=0, r=1):
        self.cx=cx
        self.cy=cy
        self.r=r
        
circles=[circle(cx=rnd.randint(1,25),
                cy=rnd.randint(1,25)) for i in range(25)]
