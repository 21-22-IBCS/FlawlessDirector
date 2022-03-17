from graphics import*
from tile import*


class squareButton():
    pos, child = 0, []

    def __init__(self, win, color, text, center, size,x,y):
        self.__class__.child.append(self)
        self.pos = self.__class__.pos
        self.__class__.pos += 1
        self.x, self.y = x,y
        self.occupy = None
        self.tile = None
        self.w = win
        self.p1 = Point(center.x - size, center.y - size)
        self.p2 = Point(center.x + size, center.y + size)
        self.r = Rectangle(self.p1, self.p2)
        self.r.draw(win)
        self.r.setFill(color)
        self.center = center
        self.t = Text(center, text)
        self.t.setSize(9)
        self.t.draw(win)

    

    def changeColor(self, newColor):
        self.r.setFill(newColor)

    @classmethod
    def isClick(cls,m):
        #print(m)
        for b in cls.child:
            #print(b)
            if(b.isClicked(m)):
                #b.r.setFill("Green")
                return b
                
    

    def isClicked(self, p):
        minX = self.p1.x
        maxX = self.p2.x
        minY = self.p1.y
        maxY = self.p2.y

        if p.x > minX:
            if p.x < maxX:
                if p.y > minY:
                    if p.y < maxY:
                        return True
                    
        return False
    
    def setText(self, text):
        self.t.setText(text)

    def getCenter(self):
        return self.center

    def setTile(self, x):
        if(self.tile != None):
            self.tile.undraw()
        self.tile = x

    def getLoc(self):
        return (self.x, self.y)
    def removeTemp(self):
        #self.tile.undraw()
        if(self.tile != None):
            self.tile.undraw()
        self.tile = None

        
