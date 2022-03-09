from graphics import*
import random
import time
from Terrain import Terrain
from Ball import Ball


def collide(points, p:Ball, win):
    pIB = []
    

    pointsInBall = p.generateInternalPoints()

    check = bool(set(points) & set(pointsInBall))
    
    if(check):
        ok = (set(points)&set(pointsInBall))
        ok = list(ok)
        length = len(ok)
        averageX = sum(map(lambda x: x[0], ok))/length
        averageY = sum(map(lambda x: x[1], ok))/length
        #line = Line(p.getLoc(), Point(averageX, averageY))
        print(averageY/averageX)
        #line.setOutline("Red")
        #line.draw(win)
        p.updateVel(averageX,averageY)
        #return 0
        
        
    return 1
    
    

def main():
    win = GraphWin("Spring Simulator", 500,500)
    #-----------
    t = Terrain(win)

    
    for i in range(3):
        t2 = Terrain(win)
        t.average(t2)
        
    t.draw(win)
    
    
    terrainPoints = t.getInternalPoints()
    #print(terrainPoints)

    #return 0
    #-----------
        
    balls = []
    for i in range(1):
        balls.append(Ball(Point(100,100), 10, win))
        
    
    

    
    ticks:int = 0
    while True:
        time.sleep(0.01)
        ticks+=1
        
        for b in balls:
            b.update()
            a = collide(terrainPoints, b, win)
            if (a == 0):
                return 0
            
    





if __name__ == "__main__":
    main()
