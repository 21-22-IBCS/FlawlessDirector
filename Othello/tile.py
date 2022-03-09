from graphics import*
from squareButton import*

class Tile():

    def __init__(self, win, center, color):
        self.t = Circle(center, 25)
        self.t.setFill(color)
        self.win = win
        self.t.draw(self.win)

    def redraw(self):
        self.t.redraw()
        
