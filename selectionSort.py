
#less efficient sort that swaps every time a lower number is found
'''
def selectSortAlt(a):

    for i in range(0,len(a)-1):
        
        for j in range(i+1, len(a)):
            if(a[j] <= a[i]): 
                a[j], a[i] = a[i], a[j]


    return a
'''

#Grade this one. This is the selection sort.
def selectSort(a):

    lowestNum = 0
    lowestIndex = 0
    for i in range(0,len(a)-1):
        lowestNum = a[i]
        lowestIndex = i
        
        for j in range(i+1, len(a)):
            if(a[j] <= lowestNum):
                lowestIndex = j
                lowestNum = a[j]
                #a[j], a[i] = a[i], a[j]
        a[lowestIndex], a[i] = a[i], a[lowestIndex]
        #if you dont like how i swap here is an alternative
                
        #another reason for the alternative is so i don't fall into
        #the comfort of convenient python functions
        '''
        temp = a[j]
        a[j] = a[i]
        a[i] = temp
        '''

    return a

def main():
    
    inputU = list(input("a: "))
    a = inputU
    print("Selection Sort")
    print(selectSort(inputU))



if __name__ == "__main__":
    main()
