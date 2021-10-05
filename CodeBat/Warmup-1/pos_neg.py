def main():
    def pos_neg(a,b,negative):
        if(abs(a) == a and abs(b) != b and negative != True):
            return True
        elif(abs(a) != a and abs(b) == b and negative != True):
            return True
        elif(negative and abs(a) != a and abs(b) != b):
            return True
        else:
            return False



if __name__ == "__main__":
    main()
