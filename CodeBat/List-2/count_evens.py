def main():

    findEven = []
    done = False


    while (done != True):
        num = input("enter number, to stop type STOP: ")
        if(num == "STOP"):
            break
        try:
            num = int(num)

        except ValueError:
            continue
        findEven.append(num)


    count = 0

    for i in range(0, len(findEven)):
        if(findEven[i] % 2 == 0):
            count += 1

    print(count)
    





if __name__ == "__main__":
    main()
