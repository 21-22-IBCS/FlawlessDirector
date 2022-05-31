from Simulation import*
import time

class Minimax():

    def __init__(self, board, player, depth):
        
        num = board.occupiedSpacesP1 if player == 1 else board.occupiedSpacesP2
        player2 = 2 if player == 1 else 1

        #print("muahuahuhuaa")
        
        b = []
        k = []
        for i in board.convert:
            k.append(i.copy())
        for i in k:
            b.append(i[len(i)-1])
        '''
        for i in k:
            b.append(i[len(i)-1])
            '''
        
        bestScore = -float('inf')
        bestPoint = None
        start = time.time()
        
        for i in b:
            
            croop = Simulation(board.win, board, 0)
            croop.doUpdate(i, player, k)
            
            
            tempScore = self.alphaBeta(croop, player, depth-1, False, -float('inf'), float('inf'))
            
            #print(tempScore)
            if(tempScore > bestScore):
                bestScore = tempScore
                bestPoint = i
        #del board
        
        self.bestmove = bestPoint
        
        board.doUpdate(self.bestmove, player, k)
        board.doAll(player,True)
        
        
        
        print("Time: " + str(time.time()-start))
        print("Best Score: " + str(bestScore))
        print("Best Move: " + str(bestPoint))


        

    def alphaBeta(self, node, player, depth, done, alpha, beta):
        #print("depth after")
        #print(depth)
        #print(done)
        #print()


        

        mainPlayer = node.occupiedSpacesP1 if player == 1 else node.occupiedSpacesP2
        otherPlayer = node.occupiedSpacesP2 if player == 1 else node.occupiedSpacesP1
        player2 = 2 if player == 1 else 1
        
        #if(len(mainPlayer) == 0
        
        if ((depth == 0 or node.isFinished())):
            crazy = node.doAll(player, False)
            #print(crazy)
            
            return crazy
        

        #print(done)
        #print(len(node.checkValidPlay(mainPlayer, player2)))
        

        if((done and len(node.checkValidPlay(mainPlayer, player2)) == 0) or (not done and len(node.checkValidPlay(otherPlayer, player)) == 0)):
            
            return self.alphaBeta(node, player, depth-1, not done, alpha,beta)
        '''
        print("depthAfter the check thingy")
        print(depth)
        print(done)
        print()
        '''
        score = 0

        if(done):

            #print("this is alsoaosaosososaos what b is")

            
            
            score = -float('inf')
            b = []
            k = node.checkValidPlay(mainPlayer, player2)
            for i in k:
                b.append(i[len(i)-1])

            for i in b:
                start = time.time()
                gloob = Simulation(node.win, node, 0)
                #print(time.time()-start)
                gloob.doUpdate(i, player, k)
            

                tempScore = self.alphaBeta(gloob, player, depth-1, False, -float('inf'), float('inf'))
                
                
                if(tempScore > score):
                    score = tempScore
                if(score > alpha):
                    alpha = score
                if(beta <= alpha):
                    break
            
                
                #del board
        
        else:
            
            
            #print("muahuahuhuaa")
            score = float('inf')
            b = []
            k = node.checkValidPlay(otherPlayer, player)
            for i in k:
                b.append(i[len(i)-1])

            
            #print(b)
            
            for i in b:
                
                gronk = Simulation(node.win, node, 0)
                
                
                gronk.doUpdate(i, player2, k)

                #print("depth")
                #print(depth)
                tempScore = self.alphaBeta(gronk, player, depth-1, True, -float('inf'), float('inf'))
                
                #print("muahuahuhuaa")
                #print(tempScore)
                
                if(tempScore < score):
                    score = tempScore
                if(score < beta):
                    beta = score
                if(beta <= alpha):
                    break
            
        #print("heheheheeheheheheh")
        return score
            
        
