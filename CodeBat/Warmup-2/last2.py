def main():
    def last2(yep):
        if (len(yep) < 3):
            return 0
        last = yep[len(yep)-2] + yep[len(yep)-1]

        howMany = 0

        for i in range(0,len(yep) - 1):
            if(i == len(yep) - 2):
                break
            current = yep[i] + yep[i+1]
            if(current == last):
                howMany += 1
        return howMany



if __name__ == "__main__":
    main()
    
