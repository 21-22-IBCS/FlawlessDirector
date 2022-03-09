from Terrain import Terrain
import random
from graphics import*
import time
from Vector import*

class Ball():
    def __init__(self, startingLoc:Point, size:int, win:GraphWin):
        self.loc = startingLoc
        self.size = size
        self.win = win
        self.shape = Circle(self.loc, self.size)
        self.shape.draw(self.win)

        self.vec = Vector(0,0)
        self.dx = 0.3
        self.dy = 0
        self.basisPoints = []
        
    def generateInternalPoints(self):
        #print("a")
        if len(self.basisPoints) == 0:
            print("abbb")
            r = range(-self.size, self.size)
            for x in r:
                for y in r:
                    if x**2 + y**2 < self.size  * (self.size):
                        self.basisPoints.append((x,y))
        arr = self.basisPoints.copy()
        
        arr[:] = map(lambda x: (round(x[0]+self.loc.x), round(x[1]+self.loc.y)), arr)
        return arr

        


    def update(self):
        self.vec.y += 0.2
        p = self.loc

        if p.getY() + self.size > self.win.height or p.getY() + self.size < 0:
            self.vec.y *= -1*0.8
            self.vec.y -= self.dy/8

        if(p.getX() + self.size > self.win.width or p.getX() + self.size < 0):
            self.vec.x *= -1*0.8

        
            


        self.shape.move(self.vec.x, self.vec.y)
        self.loc = self.shape.getCenter()
        #self.updateVel(0,0)
        


        
    def updateVel(self,aveX, aveY):
        originalX = self.vec.x
        originalY = self.vec.y

        
        vectorA = Vector(self.loc.x-aveX, self.loc.y-aveY)
        mag = math.sqrt(self.vec.getX()**2+self.vec.getY()**2)
        vectorA = Vector(vectorA.getX()*mag/5, vectorA.getY()*mag/5)
        self.vec = vectorA
        print(self.vec.getX())
        
        
        
        #normal = self.vec.normalize()
        yep = originalY / self.vec.y
        end = Point((self.vec.x*self.size) + self.loc.x, (self.vec.y*self.size) + self.loc.y)
        #l = Line(self.loc, end)
        #l.setOutline("Red")
        #l.draw(self.win)
        
        wX = aveX - end.x
        wY = aveY - end.y

        #goPoint = Line(self.loc, Point(wX,wY))
        #goPoint.setOutline("Blue")
        #goPoint.draw(self.win)
        
        
        

    
    
    def getLoc(self):
        return self.loc
    
