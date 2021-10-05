def main():
    def diff21(n):
        if(n > 21):
            return (abs(n - 21)*2)
        else:
            return abs(n - 21)


    userIn = int(input("input a number: "))

    print (diff21(userIn))



if __name__ == "__main__":
    main()
