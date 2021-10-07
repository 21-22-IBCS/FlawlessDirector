#Class for keeping track of coffee orders

#A class in Object Oriented Programming(OOP) is used for creating "Objects" which has properties that the object would have




class coffeeShopClass:
    #class variable that is tracked throughout the class
    
    totalOrders = 0
    
    #constructor for creating the coffee shop
    '''steps
1. add 1 to static order tracker
2. make current order equal to the static order tracker
3. print order by calling coffeeShop method
4. ask if user wants to make a new order by recursion

Recursion is when a function calls itself. Usually recursion is used until a statement is true, in this case it creates a coffee shop until the user stops.
'''
    #This is a constructor, it is used when an instance of a class is created
    
    def __init__(self):
        coffeeShopClass.totalOrders += 1
        self.orderNumber = coffeeShopClass.totalOrders
        print(self.coffeeShop())
        if(input("Type \"YES\" to make another order, else press return: ") == "YES"):
            newCoffee = coffeeShopClass()
            

    #coffeeShop method for making order
    '''steps
1. ask for user name
2. loop asking for coffees until user types "DONE"
3. add order to recipt
'''
#break is used to stop a loop 
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

#convert to lower case because case does not matter
def palindrome(str):
    str = str.lower()
    if(str == str[::-1]):
        return True
    return False


'''  
A nested loop is a loop within a loop. The loop inside of the outer loop executes fully before the outer loop executes again.
'''
def gcs(str1, str2):
    longestString = ""
    storeStr1 = []
    storeStr2 = []
    
    for i in range(0,len(str1)):
        for j in range(i +1, len(str1)+1):
            storeStr1.append(str1[i:j])

    for i in range (0,len(str2)):
        for j in range(i + 1, len(str2)+1):
            storeStr2.append(str2[i:j])

    for i in range(0, len(storeStr1)):
        #print (storeStr1[i])
        for j in range(0, len(storeStr2)):
            
            if(storeStr1[i] == storeStr2[j] and len(storeStr1[i]) > len(longestString)):
                longestString = storeStr1[i]
                
            
            

                        
                        
    return longestString



            


def main():

    keepTesting = True
    #User input to choose what to test.
    #try and except are used in the event that the user does not input a int so when there is a ValueError it loops back to the user input
    #A while loop keeps looping while the condition is true
    #An elif is used in the event that prior if/elif statements fail it checks that statement instead
    #continue is used to iterate to the next iteration of the loop before the rest of the code is executed
    while (keepTesting):
        try:
            
            whichTest = int(input("What would you like to test?\n1. CoffeeShop  2. Palindrome Test  3. Return Greatest Common Substring  4. End Testing\n"))
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
                userString1 = input("Input the first string: ")
                userString2 = input("Input the second string: ")
                gcsString = gcs(userString1, userString2)
                if(gcsString == ""):
                    print("Greatest common substring not found between " + userString1 + ", and " + userString2)
                else:
                    print("The greatest common substring between " + userString1 + ", and " + userString2 + " is: " + gcsString)
            elif(whichTest == 4):
                break
            else:
                print("Invalid Selection")
        except ValueError:
            print("Invalid Selection")
            continue
        
            
    
        
    
    

    
    
    



if __name__=="__main__":
    main()
