def main():
    
    def count_code(yep):
        count = 0
        for i in range(0,len(yep)-3):
            string = yep[i] + yep[i+1] + yep[i+3]
            if(string == "coe"):
                count += 1
        return count
            
        

if __name__=="__main__":
    main()
