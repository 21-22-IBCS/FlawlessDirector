import random

def main():

    def userInput():
        print()

        print("Choose what you would like to test?")
        print()

        print("1. Palindrome\n2. Haiku\n3. Tree\n4. Choose for me\n5. Terminate Program")

        userChoice = int(input("Pick a number: "))

        if(isinstance(userChoice, int) and 1 <= userChoice <= 5):
           return userChoice

        print("Invalid Selection, please choose again")
        print()

        userInput()


        

    def palindromeCheck(userWord):

        revUserWord = userWord[::-1]

        if(revUserWord == userWord):
            print("This phrase is a palindrome")
        else:
            print("This phrase is not a palindrome")

            

    def haikuCheck(userWord,userWord2,userWord3):
        vowels = ["a","e","i","o","u","A","E","I","O","U"]

        oneArray = [userWord,userWord2,userWord3]
        
        for j in range(0,3):
            vowelCount = 0
            for i in range(0, len(vowels)):
                vowelCount += oneArray[j].count(vowels[i])
            if(j == 0 and vowelCount != 5):
                print("Not a haiku, 1st line has more or less than 5 syllables")
                return False
            elif(j == 1 and vowelCount != 7):
                print("Not a haiku, 2nd line has more or less than 7 syllables")
                return False
            elif (j == 2 and vowelCount != 5):
                print("Not a haiku, 3rd line has more or less than 5 syllables")
                return False
            elif (j == 2):
                print()
                print("This is a haiku")
                return True
            
                


    def treeConvert(userWord):
        treeFormat = userWord.split()
        wordLen = len(userWord)
        print (treeFormat)

        
    terminate = False
    
    while (terminate == False):

        userChoice = userInput()
        if(userChoice == 4):
            userChoice = random.randint(1,3)
        
        if(userChoice == 1):
            word = input("Choose a word for the palindrome test: ")
            palindromeCheck(word)
        elif(userChoice == 2):
            print("Haiku format is 5,7,5 syllables for each line")

            word1 = input("Line 1: ")
            word2 = input("Line 2: ")
            word3 = input("Line 3: ")

            haikuCheck(word1, word2, word3)

        elif(userChoice == 3):
            word = input("Choose a word to convert to a tree")

            treeConvert(word)

        elif(userChoice == 5):
            terminate = True
        
        

    
        
        
        



if __name__ == "__main__":
    main()


    
