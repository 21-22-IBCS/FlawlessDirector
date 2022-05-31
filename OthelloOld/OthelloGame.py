import math
from graphics import*
from Button import*
from GameBoard import*




def main():
    win = GraphWin("OthelloGame", 400, 400)
    board = GameBoard(win, True)

    m = win.getMouse()
    while True:

        m = win.getMouse()
        board.update(m, True)
        if board.isFinished():
            print()
            print()
            print()
            print("Black: " + str(len(board.occupiedSpacesP1)))
            print("White: " + str(len(board.occupiedSpacesP2)))
            break
        
        
    


if __name__ == "__main__":
    main()
