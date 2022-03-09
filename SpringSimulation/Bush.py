from graphics import*
import random
from Terrain import Terrain

class Bush():
    def __init__(self, t:Terrain, lowerX, upperX, win:GraphWin):
        points = t.getPoints()
        z = random.randint(lowerX,upperX)

        cont = False
        for j in range(0,win.getHeight()):
            if cont:
                cont = False
                break
            for k in range(z-2,z+2):
                if(j>points[k]):
                    self.p = Point(z, j-8)
                    cont = True
                    break

        
        number = random.randrange(0,6)
        self.im = Image(self.p,"Bushes_pixelart_v00/Bush16x16_0"+str(number)+".png")

    def draw(self, win):
        self.im.draw(win)

    def undraw(self):
        self.im.undraw()

    def getPoint(self):
        return self.p