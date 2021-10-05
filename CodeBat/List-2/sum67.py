def main():
    done = False
    sum67 = []
    while (done != True):
        num = input("enter number, to stop type STOP: ")
        if(num == "STOP"):
            break
        try:
            num = int(num)

        except ValueError:
            continue
        sum67.append(num)

    
    sumOfNums = 0
    num6 = False

    for i in range(0,len(sum67)):
        if(sum67[i] == 6 and num6 == False):
            num6 = True
        if(sum67[i] == 7 and num6 == True):
            num6 = False
            continue
        if(num6 != True):
            sumOfNums += sum67[i]
    print(sumOfNums)
        
        



if __name__ == "__main__":
    main()
