#Class for keeping track of coffee orders


class coffeeShopClass:
    #class variable that is tracked throughout the class
    
    totalOrders = 0
    
    #constructor for creating the coffee shop
    '''steps
1. add 1 to static order tracker
2. make current order equal to the static order tracker
3. print order by calling coffeeShop method
4. ask if user wants to make a new order by recursion
'''
    
    def __init__(self):
        coffeeShopClass.totalOrders += 1
        self.orderNumber = coffeeShopClass.totalOrders
        print(self.coffeeShop())
        if(input("Type \"YES\" to make another order: ") == "YES"):
            newCoffee = coffeeShopClass()
            

    #coffeeShop method for making order
    '''steps
1. ask for user name
2. loop asking for coffees until user types "DONE"
3. add order to recipt
'''

    def coffeeShop(self):
        print("Welcome to the Coffee Shop!")
        userName = input("What is your name: ")
        recipt = ("-------------------\nCustomer Name: " + userName + "\n\n-----\n")
        isOrdering = True
        while(isOrdering):
            userOrder = input("What is your order, type DONE to complete your order: ")
            if(userOrder == "DONE"):
                break
            recipt += self.reciptAdd(userOrder)
        recipt += "Order Number: " + str(self.orderNumber) + "\n-------------------"
        return recipt

    def reciptAdd(self, order):
        return("Order: " + order + "\n-----\n")

    
        
#palindrome check method
#the purpose of str[::-1] is becuase it is a built in substring function. It uses the format [Start:Stop:Step]
    
#start is where in the string to start the substring
#stop is where the substring ends
#step is the value where it chooses what characters to include in the substring.
#In this case -1 == would be counting backwards from the end
def palindrome(str):
    str = str.lower()
    if(str == str[::-1]):
        return True
    return False


def main():

    keepTesting = True
    #User input to choose what to test.
    #try and except are used in the event that the user does not input a int so when there is a ValueError it loops back to the user input
    while (keepTesting):
        try:
            
            whichTest = int(input("What would you like to test?\n1. CoffeeShop  2. Palindrome Test  3. End Testing\n"))
            if(whichTest == 1):
                coffee = coffeeShopClass()
            elif(whichTest == 2):
                user = (input("Palindrome Word Test: "))
                pal = palindrome(user)
                if(pal):
                    print(user + " is a palindrome!")
                else:
                    print(user + " is not a palindrome")
                print()
            elif(whichTest == 3):
                break
            else:
                print("Invalid Selection")
        except ValueError:
            print("Invalid Selection")
            continue
        
            
    
        
    
    

    
    
    



if __name__=="__main__":
    main()
