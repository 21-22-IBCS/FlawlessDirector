def main():
    done = False
    centered = []

    while (done != True):
        num = input("enter number, to stop type STOP: ")
        if(num == "STOP"):
            break
        try:
            num = int(num)

        except ValueError:
            continue
        centered.append(num)

    if(len(centered) < 3):
        print("Array length less than 3")
        return

    #instead of using a sort algorithm im using built in array sort method  

    def centered_average(nums):
      nums.sort()
  
      smallest = nums[0]
      largest = nums[len(nums) - 1]

      print()

      print(largest)
      print()
      print(smallest)
      print()

      sumOfNums = 0
      count = 0

      large = False
      small = False

      for i in range (0, len(nums)):
          

          if(nums[i] == smallest and small == False):
              small = True
              continue

          elif(nums[i] == largest and large == False):

              large = True
              continue
        
        
          else:
              count += 1
              sumOfNums += nums[i]
          
      return int(sumOfNums/count)

    





    
    print(centered_average(centered))





if __name__ == "__main__":
    main()
