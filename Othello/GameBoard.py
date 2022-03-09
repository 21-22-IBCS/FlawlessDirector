from Button import*
from graphics import*
from squareButton import*
from Player import*
from operator import itemgetter
import math

class GameBoard():

    def __init__(self, win):
        self.win = win
        self.spaces = []
        self.visualArr = []
        self.occupiedSpacesP1 = [(3,3), (4,4)]
        self.occupiedSpacesP2 = [(3,4), (4,3)]
        self.pointsAvailable = []
        for i in range(8):
            for j in range(8):
                self.pointsAvailable.append((i,j))
        self.pointsAvailable.pop(3*8+3)
        self.pointsAvailable.pop(3*8+4)
        self.pointsAvailable.pop(4*8+3)
        self.pointsAvailable.pop(4*8+4)

        for i in range(8):
            self.visualArr.append([])
            for j in range(8):
                self.visualArr[i].append(0)

        self.visualArr[3][3] = 1
        self.visualArr[4][4] = 1
        self.visualArr[3][4] = 2
        self.visualArr[4][3] = 2

        self.direction = [(0,1),
                          (1,1),
                          (1,0),
                          (1,-1),
                          (0,-1),
                          (-1,-1),
                          (-1,0),
                          (-1,1)]
        
        
        for i in self.visualArr:
            print(i)
        #print(self.visualArr)
                
        
        for i in range(8):
            self.spaces.append([])
            for j in range(8):
                self.spaces[i].append(squareButton(self.win, "Red", str(i) + " " + str(j), Point(j*50+25, i*50+25), 25))
        self.p1 = Player(self.win, 1, self)
        
        self.p2 = Player(self.win, 2, self)
        
        self.checkValidPlay()
        

    def update(self, m):
        squareButton.isClick(m)

    def getPos(self, x):
        return self.spaces[x[0]][x[1]].getCenter()

    def checkValidPlay(self):
        yep = self.visualArr
        p1 = self.occupiedSpacesP1
        p2 = self.occupiedSpacesP2
        
        
        
        
        
    
         
