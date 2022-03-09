import math

class Vector():

    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def add(self, x , y):
        self.x += x
        self.y += y 

    def normalize(self):
        a = self.invSqrt(self.x**2 + self.y**2)
        self.x *= a
        self.y *= a

    def invSqrt(self, x):
        return 1/math.sqrt(x)
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def makeNeg(self):
        self.x *= -1.0 if self.x > 0.0 else 1.0
        self.y *= -1.0 if self.y > 0.0 else 1.0