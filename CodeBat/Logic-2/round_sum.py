def main():
    def round_sum(a,b,c):
        arr = [a,b,c]
        total = 0
        for i in range(0,3):
            if(arr[i]%10 >= 5):
                arr[i] = arr[i]+10-(arr[i]%10)
            elif(arr[i]%10 < 5):
                arr[i] = arr[i]-(arr[i]%10)

        for i in range(0,3):
            total += arr[i]
        return total
    print(round_sum(6,4,4))

if __name__=="__main__":
    main()
