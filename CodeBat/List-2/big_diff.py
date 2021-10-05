import sys

def main():
    big_diff = []
    done = False

    
    while (done != True):
        num = input("enter number, to stop type STOP: ")
        if(num == "STOP"):
            break
        try:
            num = int(num)

        except ValueError:
            continue
        big_diff.append(num)

    largest = -sys.maxsize - 1
    smallest = sys.maxsize - 1

    for i in range (0,2):
        for j in range(0,len(big_diff)):
            if (i == 0 and big_diff[j] > largest):
                largest = big_diff[j]
            if ( i == 1 and big_diff[j] < smallest):
                smallest = big_diff[j]

    diff = largest - smallest

    print (diff)
                

    

    





if __name__ == "__main__":

    main()
