def main():
    def xyz_there(yep):
        last = 0
        if(yep.find("xyz") == -1):
            return False
        for i in range(0,yep.count("xyz")):
            
            if(yep.find("xyz", last) == 0):
                return True
            elif(yep[yep.find("xyz", last) - 1] != "."):
                return True
            last = yep.find("xyz",last) + 1
            
        
        return False


if __name__=="__main__":
    main()
