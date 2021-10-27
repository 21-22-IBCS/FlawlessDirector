import time
import random

def mergeSort(li2):
    if len(li2) > 1:
        m = len(li2)//2
        left = li2[:m]
        right = li2[m:]
        mergeSort(left)
        mergeSort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li2[k] = left[i]
                i += 1
            else:
                li2[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            li2[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            li2[k] = right[j]
            j += 1
            k += 1

def selectionSort(li):
    sortedList = []
    while len(li) > 0:
        minE = li[0]
        for i in range(len(li)):
            if li[i] < minE:
                minE = li[i]
        li.pop(li.index(minE))
        sortedList.append(minE)

    return sortedList
        
            
def makeArr(length):
    re = []
    for i in range(length):
        re.append(random.randint(1,length))
    return re

def main():
    selectTime = []
    mergeTime = []
    sizes = [100,200,300,1000,5000]
    results = [["  ","[Size 100] ", "[Size 200] ", "[Size 300] ", "[Size 1000] ", "[Size 5000] "],
               ["Selection"],
               ["Merge"]]
    
    for h in range(0,2):
        for i in range(len(sizes)):
            current = makeArr(sizes[i])
            holder = []
            if(h == 0):
                for j in range(0,10):
                    start = time.time()
                    selectionSort(current.copy())
                    holder.append(time.time()-start)
                ave = 0
                for j in range(len(holder)):
                    ave += holder[j]
                results[1].append(ave/len(holder))
            elif(h == 1):
                for j in range(0,10):
                    start = time.time()
                    mergeSort(current.copy())
                    holder.append(time.time()-start)
                ave = 0
                for j in range(len(holder)):
                    ave += holder[j]
                results[2].append(ave/len(holder))
    
    print(results[0])
    print(results[1])
    print(results[2])
    
    
if __name__ == "__main__":
    main()
