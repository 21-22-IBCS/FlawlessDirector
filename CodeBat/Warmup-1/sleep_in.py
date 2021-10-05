def main():

    

    

    def sleep_in(weekday, vacation):
        if(vacation or (weekday != True)):
            print("You get to sleep in")
        else:
            print("You do not get to sleep in")
        

    userInputWeek = (input("Is weekday?\n"))
    userInputVac = (input("Vacation?\n"))

    weekBool = False
    vacBool = False

    if(userInputWeek.casefold() == "true"):
        weekBool = True
    if(userInputVac.casefold() == "true"):
        
        vacBool = True

    sleep_in(weekBool, vacBool)

    

    
    



if __name__ == "__main__":
    main()
