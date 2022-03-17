from Button import*
from graphics import*
from squareButton import*
from Player import*
#from operator import itemgetter
import math
import random
#import time


class GameBoard():

    def __init__(self, win, aiStart):
        
        self.win = win
        self.lastPlayed = None
        self.lastPlayedPoint = (0,0)
        self.spaces = []
        self.visualArr = []
        self.occupiedSpacesP1 = [(3,4), (4,3)]
        self.occupiedSpacesP2 = [(3,3), (4,4)]
        self.potential = []
        self.potentialOther = []
        self.convert = []
        self.internalCounter = 1

        self.turn = "p1"
        self.aiStart = aiStart
        

        for i in range(8):
            self.visualArr.append([])
            for j in range(8):
                self.visualArr[i].append(0)

        self.visualArr[3][4] = 1
        self.visualArr[4][3] = 1
        self.visualArr[3][3] = 2
        self.visualArr[4][4] = 2

        self.totalTurns = 1
        
                



        
        for i in range(8):
            self.spaces.append([])
            for j in range(8):
                self.spaces[i].append(squareButton(self.win, "Green", str(i) + " " + str(j), Point(j*50+25, i*50+25), 25,i,j))

        for i in self.visualArr:
            print(i)

        print("\n\n\n\n\n")

        
        if(aiStart):
            self.playerAI = 1
            self.playerHuman = 2
            self.convert = self.checkValidPlay(self.occupiedSpacesP1, 2)
            self.update(0,False)
        else:
            self.playerAI = 2
            self.playerHuman = 1
            self.convert = self.checkValidPlay(self.occupiedSpacesP1, 2)
            
            
        
        
        


        for i in self.visualArr:
            print(i)
        
        self.updateBoard()
        

    def update(self, m, tOf):
        
        theSilly = 0
        
        if(tOf):
            theSilly = squareButton.isClick(m).getLoc()

        print(self.totalTurns)
         
        
        if(((self.totalTurns%self.playerHuman == 0 and self.playerHuman == 2) or (self.totalTurns%self.playerAI != 0)) and (theSilly in self.potential) and (theSilly not in list(set(self.occupiedSpacesP1)|set(self.occupiedSpacesP2)))):
            print("sillyhaha")
            self.doUpdate(theSilly, self.playerHuman)

            ok = self.occupiedSpacesP2 if self.playerHuman == 1 else self.occupiedSpacesP1
            

            
            self.convert = self.checkValidPlay(ok, self.playerHuman)


            if(len(self.convert) == 0):
                print("hihiiiihihihihihihihihihihihihih")
                other = self.occupiedSpacesP1 if self.playerHuman == 1 else self.occupiedSpacesP2
                self.convert = self.checkValidPlay(other, self.playerAI)
                self.updateBoard()
                return 0
            
            self.totalTurns += 1
            self.lastPlayedPoint = theSilly
            self.updateBoard()
            
        if((self.totalTurns%self.playerAI == 0 and self.playerAI == 2) or (self.totalTurns%self.playerHuman != 0)):

            
            
            s = Simulation(self.win, self, self.playerAI)
            tinyAmount = Minimax(s, s.player, 4)
            self.doUpdate(tinyAmount.bestmove, self.playerAI)
            self.updateBoard()
            
            ok = self.occupiedSpacesP2 if self.playerAI == 1 else self.occupiedSpacesP1

            self.convert = self.checkValidPlay(ok, self.playerAI)
            #self.totalTurns += 1
            
            self.lastPlayedPoint = tinyAmount.bestmove
            del s
            del tinyAmount
            
            if(len(self.convert) == 0):
                print("ithadto")
                other = self.occupiedSpacesP1 if self.playerAI == 1 else self.occupiedSpacesP2
                self.convert = self.checkValidPlay(other, self.playerHuman)
                self.updateBoard()
                temporary = self.totalTurns
                self.update(0, False)
                self.totalTurns = temporary
                
            
            self.updateBoard()
            
        
        
        
        
        for i in self.visualArr:
            print(i)
        #theSilly = self.potential[0] if len(self.potential) == 1 else self.potential[random.randint(0,len(self.potential)-1)]
        
        
            
        self.updateBoard()
        self.totalTurns += 1
        self.turn = "p1" if self.totalTurns%2 == 0 else "p2"
        print(self.potential)
        
        
    def getPos(self, x):
        return self.spaces[x[0]][x[1]].getCenter()

    def checkAllDirection(self, dire, convert, p1, num):
            for i in p1:
                i = list(i)
                
                
                if (i[0] + dire[0] < 8 and i[1] + dire[1] < 8 and self.visualArr[i[0] + dire[0]][i[1] + dire[1]] == num):
                    
                    temp = []
                    while ((i[0] + dire[0] < 8 and i[0] + dire[0] > -1) and (i[1] + dire[1] < 8 and i[1] + dire[1] > -1)):
                        i[0] = i[0] + dire[0]
                        i[1] = i[1] + dire[1]
                        if(self.visualArr[i[0]][i[1]] == 0):
                            temp.append((i[0],i[1]))
                            convert.append(temp)
                            break
                        elif(self.visualArr[i[0]][i[1]] == self.visualArr[p1[0][0]][p1[0][1]]):
                            break
                        else:
                            temp.append((i[0],i[1]))
                        
                        
            return convert
        
    def doUpdate(self, silly, num):
        changeTile = []
        newList = []
        for i in range(len(self.convert)):
            if silly == self.convert[i][len(self.convert[i])-1]:
                changeTile.append(self.convert[i])
                newList = set(newList) | set(self.convert[i])
                newList = list(newList)
            for i in changeTile:
                for j in i:
                    
                    self.visualArr[j[0]][j[1]] = num

        
        if silly in self.potential:
            silly = [silly]
            self.potential = (set(silly)^set(self.potential))
            self.potential = list(self.potential)
            for i in self.potential:
                self.visualArr[i[0]][i[1]] = 0

        
        self.convert = []
        self.potential = []
        self.updateBoard()
        return self.visualArr
        
    def checkValidPlay(self, p2, num):
        convert = []
        
        
        convert = self.checkAllDirection((0,1), self.convert, p2, num)
        convert = self.checkAllDirection((1,1), self.convert, p2, num)
        convert = self.checkAllDirection((1,0), self.convert, p2, num)
        convert = self.checkAllDirection((1,-1), self.convert, p2, num)
        convert = self.checkAllDirection((0,-1), self.convert, p2, num)
        convert = self.checkAllDirection((-1,-1), self.convert, p2, num)
        convert = self.checkAllDirection((-1,0), self.convert, p2, num)
        convert = self.checkAllDirection((-1,1), self.convert, p2, num)

        for i in convert:
            self.visualArr[i[len(i)-1][0]][i[len(i)-1][1]] = num + 5
            self.potential.append((i[len(i)-1][0],i[len(i)-1][1]))

        
        
        return convert
                    
                    
        
        
        


    def updateBoard(self):
        self.occupiedSpacesP1 = []
        self.occupiedSpacesP2 = []
        for i in range(len(self.visualArr)):
            for j in range(len(self.visualArr[i])):
                if(self.visualArr[i][j] == 1):
                    self.occupiedSpacesP1.append((i,j))
                    self.spaces[i][j].setTile(Tile(self.win, self.getPos((i,j)), "Black", True))
                    continue

                elif(self.visualArr[i][j] == 2):
                    self.occupiedSpacesP2.append((i,j))
                    self.spaces[i][j].setTile(Tile(self.win, self.getPos((i,j)), "White", True))
                    continue
                    
                elif(self.visualArr[i][j] == 6):
                    self.spaces[i][j].setTile(Tile(self.win, self.getPos((i,j)), "Black", False))
                    continue
                    
                elif(self.visualArr[i][j] == 7):
                    self.spaces[i][j].setTile(Tile(self.win, self.getPos((i,j)), "White", False))
                    continue

                elif(self.visualArr[i][j] == 0):
                    
                    self.spaces[i][j].removeTemp()

        self.updateLastPlayed(self.lastPlayedPoint)
                
    

    
                                              
    def updateLastPlayed(self,p):
        if(self.lastPlayed != None and p != None):
            self.lastPlayed.undraw()
            self.lastPlayed = Circle(self.spaces[p[0]][p[1]].getCenter(), 5)
            self.lastPlayed.setFill("Red")
            self.lastPlayed.draw(self.win)
        elif(p == None):
            return 0
        else:
            self.lastPlayed = Circle(self.spaces[p[0]][p[1]].getCenter(), 5)
            self.lastPlayed.setFill("Red")
            self.lastPlayed.draw(self.win)
        
    def isFinished(self):
        if (len(self.occupiedSpacesP1) + len(self.occupiedSpacesP2) == 64):
            return True
                
    def getCurrentPlay(self):
        return (len(self.occupiedSpacesP1) + len(self.occupiedSpacesP2))-3
        
                    
                    
        
        
        
from Simulation import*
from Minimax import*
