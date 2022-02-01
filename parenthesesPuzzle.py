'''
Class for finding permutations

Purpose of a class in this scenario is to keep track of permutations
in a 2D array through a class variable
'''
class findAll:
    #global variable which is a list
    globalVar = []
    
    def __init__(self,x,arr,i):
        self.findAllBinary(x,arr,i)

    def addArr(self,arr, n):
        
        yes = []
        for i in range(0, n):
            yes.append(arr[i])
        findAll.globalVar.append(yes)

        
    def findAllBinary(self,num,arr,index):
        if num == index:
            
            self.addArr(arr,num)
            return
        arr[index] = 0
        self.findAllBinary(num, arr, index+1)
        arr[index] = 1
        self.findAllBinary(num, arr, index+1)

    def getVar(self):
        return findAll.globalVar



def searchPar(x):
    
    check = []
    ok = []
    
    for i in range(0,x):
        ok.append(None)
        ok.append(None)
    
        
    new = findAll(len(ok),ok,0)
    perms = new.getVar()

    
    for i in range(len(perms)):
        
        oops = False
        correct = []
        toScan = list(perms[i])
        if(toScan.count(0) != toScan.count(1)):
            continue
        while (len(toScan) >= 1):
            try:
                if(toScan[0] == 0):
                    correct.append(toScan.pop(0))
                    continue
                elif(toScan[0] == 1):
                    correct.pop(len(correct)-1)
                    toScan.pop(0)
                    
                    
                    continue
            except IndexError:
                oops = True
                break
        if(oops):
            continue
        check.append(perms[i])
        

    return toString(check)
            
def toString(x):
    str = ""
    for i in x:
        for j in range(0, len(i)):
            
            if i[j] == 0:
                str += "("
            elif i[j] == 1:
                str += ")"
        str += " "
    #print("yep")
    return str

def main():
    userInput = int(input("num: "))
    print(searchPar(userInput))

    



if __name__=="__main__":
    main()
    
