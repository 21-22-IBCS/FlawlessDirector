def main():
    def date_fashion(you,date):
        if((you >= 8 or date >= 8) and (you <= 2 or date <= 2) != True):
            return 2
        elif(you <= 2 or date <= 2):
            return 0
        else:
            return 1
if __name__=="__main__":
    main()
