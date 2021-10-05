def main():
    def alarm_clock(day,vacation):
        if(1 <= day <= 5 and vacation != True):
            return "7:00"
        elif(vacation and (day == 0 or day ==6)):
            return "off"
        else:
            return "10:00"
            


if __name__=="__main__":
    main()
    
