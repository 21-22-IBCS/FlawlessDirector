import math
import time
from GameBoard import GameBoard


class Simulation(GameBoard):
    
    theWeights = []

    def __init__(self, win,b, look):
        self.win = win
        self.copyAll(b)
        self.weights = [[100,-10,8,6,6,8,-10,100],
                        [-10,-25,-4,-4,-4,-4,-25,-10],
                        [8,-4,6,4,4,6,-4,8],
                        [6,-4,4,0,0,4,-4,6],
                        [6,-4,4,0,0,4,-4,6],
                        [8,-4,6,4,4,6,-4,8],
                        [-10,-25,-4,-4,-4,-4,-25,-10],
                        [100,-10,8,6,6,8,-10,100]]

        self.valuesForLerp = [
                    [8, 85, -40, 10, 210, 520],
                    [8, 85, -40, 10, 210, 520],
                    [33, -50, -15, 4, 416, 2153],
                    [46, -50, -1, 3, 612, 4141],
                    [51, -50, 62, 3, 595, 3184],
                    [33, -5,  66, 2, 384, 2777],
                    [44, 50, 163, 0, 443, 2568],
                    [13, 50, 66, 0, 121, 986],
                    [4, 50, 31, 0, 27, 192],
                    [8, 500, 77, 0, 36, 299]]


        self.valuesInbetween = [0, 55, 56, 57, 58, 59, 60, 61, 62, 63]

        self.player = look
            
        



    def doAll(self, player, gogo):
        score = 0

        m = self.occupiedSpacesP1 if player == 1 else self.occupiedSpacesP2
        other = self.occupiedSpacesP2 if player == 1 else self.occupiedSpacesP1

        if(len(m) == 0):
            return 0

        if(len(other) == 0):
            return 1000000


        
        
        weigh = Simulation.theWeights[len(m) + len(other)]
        
        
        test1 = self.amountTake(player)
        test2 = self.adjOpen(player)
        test3 = self.currentTiles(player)
        test4 = self.scoreW(player)
        test5 = self.unflippable(player)
        test6 = self.checkCorner(player)

        

        
        


        score += test1 * weigh[0]
        score += test2 * weigh[1]
        score += test3 * weigh[2]
        score += test4 * weigh[3]
        score += test5 * weigh[4]
        score += test6 * weigh[5]


        


        '''
        
        if(gogo):
             print("test1: " + str(test1))
             print("test2: " + str(test2))
             print("test3: " + str(test3))
             print("test4: " + str(test4))
             print("test5: " + str(test5))
             print("test6: " + str(test6))
             Simulation.allTests.append([test1+Simulation.allTests[len(Simulation.allTests)-1][0],
                                         test2+Simulation.allTests[len(Simulation.allTests)-1][1],
                                         test3+Simulation.allTests[len(Simulation.allTests)-1][2],
                                         test4+Simulation.allTests[len(Simulation.allTests)-1][3],
                                         test5+Simulation.allTests[len(Simulation.allTests)-1][4],
                                         test6+Simulation.allTests[len(Simulation.allTests)-1][5],
                                         self.getCurrentPlay()])

            
        


        
        '''
        
        '''
        if(self.getCurrentPlay()%6 == 0):
            print(test1)
            print(test2)
            print(test3)
            print(test4)
            print(test5)
            print(test6)
            print()

            for i in self.visualArr:
                print(i)
        
        '''

        
        return score


    
    @classmethod
    def lerp(cls, valuesForLerp, valuesInbetween):
        for i in range(65):
            Simulation.theWeights.append([0,0,0,0,0,0])
        
        for i in range(65):
            w = 0
            for j in range(len(valuesInbetween)):
                if(i <= valuesInbetween[j]):
                    w = j
                    break

            if(w == 0):
                Simulation.theWeights[i] = valuesForLerp[0]
                continue

            
            
            factor = ((float)(i - valuesInbetween[w-1]))/(valuesInbetween[w]-valuesInbetween[w-1])
            
            for j in range(len(valuesForLerp[w])):
                Simulation.theWeights[i][j] = ((int)(round(factor*valuesForLerp[w][j]) + (1-factor) * valuesForLerp[w-1][j]))
                
    

    def copyAll(self, board):
        self.occupiedSpacesP1 = board.occupiedSpacesP1.copy()
    
        self.occupiedSpacesP2 = board.occupiedSpacesP2.copy()
        
        
        
        self.potential = board.potential.copy()
        self.convert = []
        for i in board.convert:
            self.convert.append(i.copy())
        self.spaces = board.spaces.copy()
        self.visualArr = []
        
        for i in board.visualArr:
            self.visualArr.append(i.copy())
            
        self.totalTurns = board.totalTurns
        self.turn = board.turn
        
    
    def updateBoard(self):
        self.occupiedSpacesP1 = []
        self.occupiedSpacesP2 = []
        for i in range(len(self.visualArr)):
            for j in range(len(self.visualArr[i])):
                if(self.visualArr[i][j] == 1):
                    self.occupiedSpacesP1.append((i,j))
                    
                if(self.visualArr[i][j] == 2):
                    self.occupiedSpacesP2.append((i,j))
                      
        
    def getPlayerScore(self, num):
        if(num == 1):
            return len(self.occupiedSpacesP1)
        elif(num == 2):
            return len(self.occupiedSpacesP2)
    
    def checkCorner(self, z):
        m = self.occupiedSpacesP1 if z == 1 else self.occupiedSpacesP2
        other = self.occupiedSpacesP2 if z == 1 else self.occupiedSpacesP1 
        
        if ((0,0) in m): return 100
        if ((7,0) in m): return 100
        if ((0,7) in m): return 100
        if ((7,7) in m): return 100
            
        return 0


    def unflippable(self, z):
        m = self.occupiedSpacesP1 if z == 1 else self.occupiedSpacesP2
        other = self.occupiedSpacesP2 if z == 1 else self.occupiedSpacesP1 

        otherLen = 0
        if(self.visualArr[0][0] == self.visualArr[other[0][0]][other[0][1]]): otherLen += len(self.calcOp(self.visualArr[other[0][0]][other[0][1]],(0,0)))
        if(self.visualArr[0][7] == self.visualArr[other[0][0]][other[0][1]]): otherLen += len(self.calcOp(self.visualArr[other[0][0]][other[0][1]],(0,7)))
        if(self.visualArr[7][0] == self.visualArr[other[0][0]][other[0][1]]): otherLen += len(self.calcOp(self.visualArr[other[0][0]][other[0][1]],(7,0)))
        if(self.visualArr[7][7] == self.visualArr[other[0][0]][other[0][1]]): otherLen += len(self.calcOp(self.visualArr[other[0][0]][other[0][1]],(7,7)))

        mLen = 0
        if(self.visualArr[0][0] == self.visualArr[m[0][0]][m[0][1]]): mLen += len(self.calcOp(self.visualArr[m[0][0]][m[0][1]],(0,0)))
        if(self.visualArr[0][7] == self.visualArr[m[0][0]][m[0][1]]): mLen += len(self.calcOp(self.visualArr[m[0][0]][m[0][1]],(0,7)))
        if(self.visualArr[7][0] == self.visualArr[m[0][0]][m[0][1]]): mLen += len(self.calcOp(self.visualArr[m[0][0]][m[0][1]],(7,0)))
        if(self.visualArr[7][7] == self.visualArr[m[0][0]][m[0][1]]): mLen += len(self.calcOp(self.visualArr[m[0][0]][m[0][1]],(7,7)))
        
        return 100*(mLen-otherLen)/(mLen+otherLen+1)

    def currentTiles(self, z):
        m = self.occupiedSpacesP1 if z == 1 else self.occupiedSpacesP2
        other = self.occupiedSpacesP2 if z == 1 else self.occupiedSpacesP1
        
        otherLen = len(other)
        mLen = len(m)
        #print(otherLen)
        #print(mLen)
        return 100*(mLen-otherLen)/(mLen+otherLen+1)


    
    
        
    def adjOpen(self, z):
        m = self.occupiedSpacesP1 if z == 1 else self.occupiedSpacesP2
        other = self.occupiedSpacesP2 if z == 1 else self.occupiedSpacesP1 

        otherLen = len(self.calcAdj(self.visualArr[other[0][0]][other[0][1]]))
        mLen = len(self.calcAdj(self.visualArr[m[0][0]][m[0][1]]))

        return 100*(mLen-otherLen)/(mLen+otherLen+1)

    def amountTake(self, z):
        m = self.occupiedSpacesP1 if z == 1 else self.occupiedSpacesP2
        other = self.occupiedSpacesP2 if z == 1 else self.occupiedSpacesP1
        player2 = 2 if z == 1 else 1

        

        
        mLen = 0
        #ok = self.checkValidPlay(m, self.visualArr[other[0][0]][other[0][1]])

        '''
        for i in ok:
            mLen += len(i)
        '''
        
        mLen = len(m)
        otherLen = 0
        
        never = 0
        #never = self.checkValidPlay(other, self.visualArr[m[0][0]][m[0][1]])
        
        
        '''
        for i in never:
            otherLen += len(i)
        '''
        otherLen = len(other)

        return 100*(mLen-otherLen)/(mLen+otherLen+1)


    def scoreW(self,z):
        m = self.occupiedSpacesP1 if z == 1 else self.occupiedSpacesP2
        other = self.occupiedSpacesP2 if z == 1 else self.occupiedSpacesP1
        '''
        for i in self.visualArr:
            print(i)
        '''
        mLen = 0
        for i in m:
            mLen += self.weights[i[0]][i[1]]
        otherLen = 0
        for i in other:
            otherLen += self.weights[i[0]][i[1]]
            
        return mLen-otherLen
        


    def calcAdj(self, z):
        m = self.occupiedSpacesP1 if z == 1 else self.occupiedSpacesP2
        other = self.occupiedSpacesP2 if z == 1 else self.occupiedSpacesP1
        
        valid = []

        dire = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
                
        for i in other:
            for j in dire:
                if ((i[0] + j[0] < 8 and i[0] + j[0] > -1) and (i[1] + j[1] < 8 and i[1] + j[1] > -1)):
                    if(self.visualArr[i[0]+j[0]][i[1]+j[1]] == 0):
                        valid.append((i[0]+j[0],i[1]+j[1]))
        valid = set(valid)
        valid = list(valid)

        return valid
                    
                    
            
                
        

    def calcOp(self, z, loc):
        convert = []
        m = self.occupiedSpacesP1 if z == 1 else self.occupiedSpacesP2
        other = self.occupiedSpacesP2 if z == 1 else self.occupiedSpacesP1 

        dire = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,1)]
        
        point = list(loc)
        point[0] -= 1
        while point[0] > 0:
            if (point[0] == self.visualArr[m[0][0]][m[0][1]]):
                convert.append((point[0],point[1]))
            point[0] -= 1
        
        
        for i in dire:
            l = list(loc)
            while ((l[0] + i[0] < 8 and l[0] + i[0] > -1) and (l[1] + i[1] < 8 and l[1] + i[1] > -1)):
                        l[0] = l[0] + i[0]
                        l[1] = l[1] + i[1]
                        
                        if(self.visualArr[l[0]][l[1]] == self.visualArr[other[0][0]][other[0][1]]):
                            convert.append((l[0],l[1]))
                            
            
            
        convert = set(convert)
        convert = list(convert)
        return convert

    def checkValidPlay(self, p2, num):
        
        convert = []
        
        
        convert = self.checkAllDirection((0,1), convert, p2, num)
        convert = self.checkAllDirection((1,1), convert, p2, num)
        convert = self.checkAllDirection((1,0), convert, p2, num)
        convert = self.checkAllDirection((1,-1), convert, p2, num)
        convert = self.checkAllDirection((0,-1), convert, p2, num)
        convert = self.checkAllDirection((-1,-1), convert, p2, num)
        convert = self.checkAllDirection((-1,0), convert, p2, num)
        convert = self.checkAllDirection((-1,1), convert, p2, num)

        #print(convert)
        
        
            
        '''
        for i in convert:
            #self.visualArr[i[len(i)-1][0]][i[len(i)-1][1]] = num + 5
            self.potential.append((i[len(i)-1][0],i[len(i)-1][1]))
        '''

        
        
        return convert

    def doUpdate(self, silly, num, convert):
        changeTile = []
        newList = []
        for i in range(len(convert)):
            if silly == convert[i][len(convert[i])-1]:
                changeTile.append(convert[i])
                newList = set(newList) | set(convert[i])
                newList = list(newList)
            for i in changeTile:
                for j in i:
                    
                    self.visualArr[j[0]][j[1]] = num

        
        

        
        self.convert = []
        self.potential = []
        self.updateBoard()


from Minimax import*
