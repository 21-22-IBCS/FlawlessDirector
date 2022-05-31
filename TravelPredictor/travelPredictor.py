from graphics import *
from Button import *
from Dropmenu import *
from scrollBox import *
from os.path import exists
import time
import csv

def newDaySelection(day, text1, textBox, lamb):
    dictDay = {"Mon" : "Monday", "Tu": "Tuesday", "Wed" : "Wednesday", "Th" : "Thursday", "Fri" : "Friday"}
    text1.setText(lamb(dictDay[day]))
    with open("timeTable.csv", newline='') as f:
        #fieldnames = ["Mon", "Tu","Wed", "Th","Fri"]
        reader = csv.DictReader(f)
        t = ""
        for row in reader:
            if(row[day] == ""):
                continue
            t += row[day] + "\n"
        textBox.setText(t)


def updateCSV(day, textBox, error):
    existingRow = []
    with open("timeTable.csv", "r", newline='') as f:
        
        reader = csv.DictReader(f)
        currentValues = textBox.getText()
        currentValues = currentValues.split("\n")
        
        if currentValues[len(currentValues)-1] == '':
            currentValues.pop(len(currentValues)-1)
        
        try:
            a = list(map(lambda x: x.replace(":",""), currentValues))
            if (all(x.find(", ") == -1  for x in currentValues)):
                raise Exception("Invalid Time")
            a = list(map(lambda x: x.replace(", ",""), a))
            a = list(map(lambda x: int(x), a))
            
        except:
            error.setText("INVAILD INPUT FORMAT")
            return 0
        
        end = 0
        for j, i in enumerate(reader):
            
            fieldnames = {"Mon" : i["Mon"], "Tu" : i["Tu"],"Wed" : i["Wed"], "Th" : i["Th"],"Fri" : i["Fri"]}
            if(j < len(currentValues)):
                fieldnames[day] = currentValues[j]
            else:
                fieldnames[day] = ""
            end = j
            if(set(fieldnames.values()) == {''}):
                
                continue
            
            
            existingRow.append(fieldnames)
            
        
        if(end < len(currentValues)):
            end = end+1 if len(currentValues) != 1 else end
            for i in range(end, len(currentValues)):
                fieldnames = {"Mon" : "", "Tu" : "","Wed" : "", "Th" : "","Fri" : ""}
                fieldnames[day] = currentValues[i]
                existingRow.append(fieldnames)

    with open("timeTable.csv", "w", newline='') as f:
        fieldnames = ["Mon", "Tu","Wed", "Th","Fri"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)

        writer.writeheader()
        
        
        writer.writerows(existingRow)

    error.setText("CSV File Sucessfully Updated")



    
def estimateTime(day, timeWant, textBox, error):
    with open("timeTable.csv", "r", newline='') as f:
        reader = csv.DictReader(f)
        timeWant = timeWant.split(", ")
        timeWant = list(map(lambda x: x.split(":"), timeWant))
        try:
            timeWant = (int(timeWant[0][0]) * 60) + int(timeWant[0][1])
        except:
            error.setText("Invalid Desired Arrival Time\n Please Use Format \"HOUR:MINUTE\"")
            return "ERROR"
        currentValues = []
        for row in reader:
            if(row[day] == ""):
                continue
            currentValues.append(row[day])
        entryNumber = len(currentValues)
        a = list(map(lambda x: x.split(", "), currentValues))
        minuteMean = 0
        for i in range(len(a)):
            a[i] = list(map(lambda x: x.split(":"), a[i]))
            if(a[i][0][1][0] ==  "0"):
                a[i][0][1] = a[i][0][1][1]

            elif(a[i][1][1][0] == "0"):
                a[i][1][1] = a[i][1][1][1]
                
            
            temp = (int(a[i][0][0])*60) + int(a[i][0][1])
            
            minuteMean += ((int(a[i][1][0]) * 60) + (int(a[i][1][1]))) - temp
        minuteMean /= len(a)
        timeWant -= minuteMean
        
        hourTime = int(timeWant/60)
        minuteTime = int(timeWant%60)
        minuteTime = str(0) + str(minuteTime) if len(str(minuteTime)) == 1 else minuteTime
        return str(hourTime) + ":" + str(minuteTime)


def main():
    
    win = GraphWin("Travel Predictor", 500, 500)
    
    if(not exists("timeTable.csv")):
        with open("timeTable.csv", "w", newline='') as f:
            fieldnames = ["Mon", "Tu","Wed", "Th","Fri"]
            writer = csv.DictWriter(f, fieldnames = fieldnames)
            writer.writeheader()
    
    
    csValues = scrollBox(win,Point(400,170), 20,20)
    csValues.draw(win)
    
    updateButton = Button(win, "white", "Update CSV File", Point(400,350), 50)

    estimateButton = Button(win, "white", "Estimate!", Point(80, 110), 50)
    
    userInput = Entry(Point(80,30), 20)
    userInput.setFill("gray")
    userInput.setText("Desired time. Ex. \"9:10\"")
    userInput.draw(win)

    daysList = ["Mon", "Tu", "Wed", "Th", "Fri"]
    
    daySelection = Dropmenu(win, Point(80,60), daysList[0], daysList)
    daySelection.draw(win)

    showFormat = lambda a : "Current Day Selected: " + a

    textDaySelected = Text(Point(400,10), "haha")
    textDaySelected.draw(win)

    textEstimate = Text(Point(80, 150), "Leave at: ")
    textEstimate.draw(win)

    textError = Text(Point(400,410), "")
    textError.draw(win)

    textInstruction = Text(Point(80, 250), "Make sure to update CSV file\nbefore updating.")
    textInstruction.draw(win)

    textInstruction2 = Text(Point(390, 450), "Input Values as format \"Departure, Arrival\"\nEx. \"9:10, 9:30\"")
    textInstruction2.draw(win)

    newDaySelection(daySelection.getCurrent(), textDaySelected, csValues, showFormat)
    

    
    
    


    currentDay = daySelection.getCurrent()
    m = win.getMouse()
    while True:

        
        
        if(currentDay != daySelection.getCurrent()):
            currentDay = daySelection.getCurrent()
            newDaySelection(currentDay, textDaySelected, csValues, showFormat)
        if(updateButton.isClicked(m)):
            updateCSV(currentDay, csValues, textError)
        if(estimateButton.isClicked(m)):
            textEstimate.setText("Leave at: " + str(estimateTime(currentDay, userInput.getText(), csValues, textError)))
            
            

        m = win.getMouse()
        textError.setText("")
        
           

        
        




if __name__ =="__main__":
    main()
