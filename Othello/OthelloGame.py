import math
from graphics import*
from Button import*
from GameBoard import*




def main():
    win = GraphWin("OthelloGame", 400, 400)
    board = GameBoard(win)

    m = win.getMouse()
    while True:

        m = win.getMouse()
        board.update(m)
        
        
    


if __name__ == "__main__":
    main()
