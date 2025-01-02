def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

    return alist

def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist) - 1

    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1

    return alist

def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

    return alist
        
def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        
        alist[position] = currentvalue

    return alist

def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        # print("After increments of size", sublistcount, "The list is", alist)
        sublistcount = sublistcount // 2

    return alist

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        
        while position >= gap and \
            alist[position-gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue