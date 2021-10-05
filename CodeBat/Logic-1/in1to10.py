def main():
    def in1to10(n,outside_mode):
        if (1 <= n <= 10 and outside_mode != True):
            return True
        elif(outside_mode and (n <= 1 or n >= 10)):
            return True
        else:
            return False


if __name__=="__main__":
    main()
