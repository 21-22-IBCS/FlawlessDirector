import random

#Returns the average word length
def averageWordLength(yep):
    nums = 0
    for i in yep:
        nums += len(i)
    return nums/len(yep)

#Returns the most common word
def mostCommonWord(yep):
    #Stores all words in a dictionary

    '''
    A dictionary is unordered, mutable, and does not contain duplicates.
    Values are stores with "Keys" where each key contains a value.
    The format for this is Key:Value.
    To instantiate a dictionary you use curly brackets {}
    '''
    d = {}
    for i in yep:
        #this adds 1 to the value corresponding to the key if it exists
        if i in d:
            d[i] += 1
        #otherwise add the key to the dictionary with a value of 1
        else:
            d[i] = 1
    #In order to get the largest word, variable "largest" is set to negative infinity
    largest = -(float('inf'))
    bigWord = ""
    for i in d:
        if d[i] >= largest:
            largest = d[i]
            bigWord = i
    return bigWord

#Returns the percent of conjunctions
def percentOfConjunctions(yep):
    nums = 0

    for i in yep:
        if (i == "and" or i == "but" or i == "or"):
            nums +=1

    return (nums/len(yep))*100

#Returns the longest sentence and its length
def longestSentence(yep):
    #Since sentences end with either a ".", "!", or "?", replace all instances with a "#" so when the string is split you can split all instances of "#"
    yep = yep.replace(".", "#")
    yep = yep.replace("!", "#")
    yep = yep.replace("?", "#")
    arr = yep.split("#")
    longest = -float('inf')
    index = 0
    for i in range(len(arr)):
        if len(arr[i]) >= longest:
            longest = len(arr[i])
            index = i
    return longest, arr[index] + "."
    
#Returns a sentence from words picked at random within the text
def sampleSentence(yep):
    string = ""
    #The method "capitalize()" captializes the character at index 0 in the string
    string += yep[random.randint(0,len(yep)-1)].capitalize()
    for i in range(0,10):
        string += " "
        string += yep[random.randint(0,len(yep)-1)]
    string += "."
    return string

def longestWords(arr):
    amount = {}
    for j in range(10):
        index = 0
        word = ""
        length = -float('inf')
        for i in range(len(arr)):
            if (len(arr[i]) >= length):
                index = i
                word = arr[i]
                length = len(arr[i])
        amount[word] = arr.pop(index)
    return amount

def main():
    yep = open("alice.txt", "r")
    yep = yep.read()
    yep = yep.split("[Illustration]")[1]
    yep = yep.split("THE END")[0]
    #List of all punctuation to remove
    removal = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    tempArr = yep.split()
    #Removes punctuation from strings, also sets them to lowercase
    for j in range(3):
        for i in range(len(tempArr)):
            tempArr[i] = tempArr[i].strip(removal).lower()

    
    aveWord = "Average Word Length: " + str(averageWordLength(tempArr)) + " characters"
    commonWord = "Most Common Word: " + str(mostCommonWord(tempArr))
    percent = "Percent Of Conjunctions: " +  str(percentOfConjunctions(tempArr)) + "%"
    sentenceLength, sentence = longestSentence(yep)
    sentenceLength = "Longest Sentence Length: " + str(sentenceLength) + " characters"
    sentence = "Longest Sentence:\n\n" + str(sentence)
    sample = "Sample Sentence: " + str(sampleSentence(tempArr))

    #Stores results in a dictionary
    results = {
        1: aveWord,
        2: commonWord,
        3: percent,
        4: sentence,
        5: sentenceLength,
        6: sample
        }


    run = True

    print(longestWords(tempArr))
    
    while(run):
        print("What information about this text would you like to display?\n")
        print("1. AverageWordLength 2. MostCommonWord 3. PercentOfConjunctions\n4. LongestSentence 5. LongestSentenceLength 6. SampleSentence 7. EndProgram\n")
        # "Try" is used for the event that the user does not input an integer, if one is not used "except" will run instead
        try:
            user = int(input("Please input an integer: "))
            if(user == 7):
                run = False
                break
            if(user > 7):
                print("\nInvalid Input\n\n")
                continue
            print("\n\n\n\n\n\n" + str(results[user]) + "\n\n\n\n\n\n\n")
        except ValueError:
            print("\nInvalid Integer\n\n")
            continue
            
        
    

    
    


if __name__ == "__main__":
    main()
