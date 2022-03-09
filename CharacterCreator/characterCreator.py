from graphics import*
from Button import*

def main():
    win = GraphWin("win", 800,600)

    head = Oval(Point(200,50), Point(600,550))

    eye1 = Circle(Point(350,100),25)
    eye2 = Circle(Point(450,100),25)

    eye3 = Rectangle(Point(300,100),Point(350,150))
    eye4 = Rectangle(Point(450,100),Point(500,150))
    
    eye5 = Oval(Point(300,100),Point(350,200))
    eye6 = Oval(Point(450,100),Point(500,200))



    
    head.draw(win)

    Button1 = Button(win, "white", "a", Point(100, 100), 45)
    Button2 = Button(win, "white", "b", Point(100, 150), 45)
    Button3 = Button(win, "white", "c", Point(100, 200), 45)
    
    
    current1 = eye1.clone()
    current2 = eye2.clone()

    m = win.getMouse()
    while True:
        if Button1.isClicked(m):
            current1.undraw()
            current2.undraw()
            current1 = eye1.clone()
            current2 = eye2.clone()
            current1.draw(win)
            current2.draw(win)
        if Button2.isClicked(m):
            current1.undraw()
            current2.undraw()
            current1 = eye3.clone()
            current2 = eye4.clone()
            current1.draw(win)
            current2.draw(win)
        if Button3.isClicked(m):
            current1.undraw()
            current2.undraw()
            current1 = eye5.clone()
            current2 = eye6.clone()
            current1.draw(win)
            current2.draw(win)
        

        m = win.getMouse()
    head.draw(win)
    



if __name__ == "__main__":
    main()
