def extractEachKth(inputArray, k):
    del inputArray[k-1::k]
    
    return inputArray

#print(extractEachKth([1, 2, 1, 2, 1, 2, 1, 2], 2))


print(extractEachKth([2, 4, 6, 8, 10], 2))