def main():
    def caught_speeding(speed,is_birthday):
        if(speed <= 60 or (is_birthday and speed <= 65)):
            return 0
        elif(61 <= speed <= 80 or (is_birthday and speed <= 85)):
            return 1
        elif(81 <= speed or (is_birthday and speed <=86)):
            return 2

if __name__=="__main__":
    main()
