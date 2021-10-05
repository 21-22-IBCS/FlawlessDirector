def main():
    #this solutions fails "other tests" but CodingBat does not specify what is failed
    def end_other(a,b):
        a = a.lower()
        b = b.lower()
        if(abs(len(a) - len(b)) == a.find(b)):
            return True
        elif(abs(len(b)-len(a)) == b.find(a)):
            return True
        else:
            return False


    
    


if __name__=="__main__":
    main()
