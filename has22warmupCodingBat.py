def main():

    def doesHave22(has22):
        for i in range(0,len(has22) - 1):
            if(has22[i] == 2 and (has22[i-1] == 2 or has22[i+1] == 2)):
                return True

        return False

    has22 = []
    done = False
    while (done != True):
        num = input("enter number, to stop type STOP: ")
        if(num == "STOP"):
            break
        try:
            num = int(num)

        except ValueError:
            continue
        has22.append(num)
    
    print(has22)
    
    print("does it contain a 2 next to a 2? " + str(doesHave22(has22)))
                

    






if __name__ == "__main__":
    main()
