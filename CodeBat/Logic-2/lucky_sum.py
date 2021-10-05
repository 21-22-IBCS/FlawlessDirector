def main():
    def lucky_sum(a,b,c):
        arr = [a,b,c]
        index = 3
        total = 0
        for i in range(0,len(arr)):
            if(arr[i] == 13):
                index = i
                break
        for i in range(0,index):
            total += arr[i]
        return total


if __name__=="__main__":
    main()
