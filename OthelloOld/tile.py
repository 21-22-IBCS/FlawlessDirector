from graphics import*
from squareButton import*

class Tile():

    def __init__(self, win, center, color, real):
        self.t = Circle(center, 25)
        if(real):
            self.t.setFill(color)
        self.win = win
        self.t.draw(self.win)
        self.real = real

    def redraw(self):
        self.t.redraw()
    def undraw(self):
        self.t.undraw()
    
    def getReal(self):
        return self.real
