from graphics import*
from squareButton import*
from tile import*
import math


class Player():

    def __init__(self, win, num, board):
        self.board = board
        self.win = win
        if(num == 1):
            self.color = "Black"
            self.tiles = [(3,3), (4,4)]
            self.tileObj = [Tile(self.win, self.board.getPos((j,k)), self.color) for j,k in self.tiles]
        if(num == 2):
            self.color = "White"
            self.tiles = [(3,4), (4,3)]
            self.tileObj = [Tile(self.win, self.board.getPos((j,k)), self.color) for j,k in self.tiles]

    def setNum(self, x):

        self.tiles += x


    def doesOccupy(self, x):
        if(x in self.tiles):
            return True
        
