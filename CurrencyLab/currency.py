from graphics import*
from Button import*
#imported Dropmenu, class file in folder
from Dropmenu import*

def convert(user, currentSelection):
    #Dictionary that contains conversion values
    v = {"CAD": 1.28,
         "GBP": 0.74,
         "EUR": 0.78,
         "JPY": 115.23,
         "CHF": 0.93,
         "AUD": 1.41
         }
    
    user = float(user)
    current = float(v[currentSelection])

    #multiply by 100 and cast int to move 2 decimal places to the left
    multi = int((user*current)*100)
    #round values
    if(int(((user*current)*1000)%10) >= 5):
        multi +=1
    #convert back to float
    multi = float(multi/100)
    return multi


    

def main():
    win = GraphWin("Currency Converter", 300, 200)
    close = Button(win, "white", "Quit", Point(50, 160), 45)
    convertButton = Button(win, "white", "Convert", Point(150, 160), 45)
    userInput = Entry(Point(45,50), 10)
    userInput.setFill("white")
    #contains currency options available
    alright = ["CAD","GBP","EUR","JPY","CHF","AUD"]
    #instantiates a dropdown menu
    dropMenu = Dropmenu(win, Point(135,50),alright[0], alright)
    result = Text(Point(25,70), "Result: ")
    explain = Text(Point(130, 30), "All conversions are from USD to selected currency")
    arrow = Text(Point(95,50),"-->")
    
    explain.draw(win)
    arrow.draw(win)
    dropMenu.draw(win)
    result.draw(win)
    userInput.draw(win)
    m = win.getMouse()
    while True:
        if close.isClicked(m):
            break
        if convertButton.isClicked(m):
            #check if user input is a float value
            try:
                result.setText(str(convert(userInput.getText(),dropMenu.getCurrent())) + " " + str(dropMenu.getCurrent()))
                #changes position of text to stay at the same position, this is as close as i could get it since you cannot align text
                moveAmount = ((len(str(result.getText()))-7)*3)+27
                result.move(moveAmount-result.getAnchor().x,0)
            except:
                result.setText("PLEASE ENTER VALID FLOAT")
                result.move(80-result.getAnchor().x,0)
        m = win.getMouse()
    win.close()
    
    


if __name__ == "__main__":
    main()
