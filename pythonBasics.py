
import random
def main():
    #Name of assignment and date completed

    print("pythonBasics.py")
    print(str("Date Completed: 9/21/21"))

    
    #sum of 2 nums and product of 2 nums


    #for loop that randomizes nums 1-100 twice, once for sum and another for product and stores them in an array
    #then prints the sum and product of those numbers
    for j in [0, 1]:
        nums = []
        for i in [0, 1]:
            nums = [i, random.randint(1, 100)]
        if (j == 0):
            print (nums[0] + nums[1])
        else:
            print (nums[0] + nums[1])
    
    
    #Fun Fact Page

    #initilizes an array and does a for loop 3 times 1 for each value

    student = [20, 80, 114]

    for i in [0, 1, 2]:
        print (str("There are currently ") + str(student[i]) + str(" students in the USB."))

    

    
    



if __name__ == "__main__":
    main()

