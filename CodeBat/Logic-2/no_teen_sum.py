def main():
    #CodingBat says to write a seperate helper that fixes the array
    #for the teen rule to avoid having to write the code 3 times
    #however you can use a loop for the rule so i'm unsure why you need to 
    #write a seperate helper method
    def no_teen_sum(a,b,c):
        arr = [a,b,c]
        total = 0
        for i in range(0,3):
            if(13 <= arr[i] <= 19 and arr[i] != 15 and arr[i] != 16):
                arr[i] = 0
        for i in range(0,3):
            total += arr[i]
        return total

    
            

if __name__=="__main__":
    main()
