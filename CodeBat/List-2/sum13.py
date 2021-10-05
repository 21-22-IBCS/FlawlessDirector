def main():
    '''
    The assignment does not clarify if the array is sorted or not
    so i will assume it is unsorted.
    '''
    sum13 = []
    done = False
    

    while (done != True):
        num = input("enter number, to stop type STOP: ")
        if(num == "STOP"):
            break
        try:
            num = int(num)

        except ValueError:
            continue
        sum13.append(num)
    
    if (len(sum13) == 0):
        print(0)
        return

    total = 0

    for i in range(0, len(sum13)):
        if (sum13[i] == 13):
            break
        total += sum13[i]

    print(total)




if __name__ == "__main__":
    main()
