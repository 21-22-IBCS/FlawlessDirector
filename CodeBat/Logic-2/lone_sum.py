def main():
    def lone_sum(a,b,c):
        arr = [a,b,c]
        total = 0
        if(arr.count(a) > 1):
            for i in range(0, arr.count(a)):
                arr.pop(arr.index(a))
        if(arr.count(b) > 1):
            for i in range(0, arr.count(b)):
                arr.pop(arr.index(b))
        for i in range(0,len(arr)):
            total += arr[i]
        return total
            
                
            
            
                


if __name__=="__main__":
    main()
