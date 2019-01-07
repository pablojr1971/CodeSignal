def arrayReplace(inputArray, elemToReplace, substitutionElem):
   
    for x in range(len(inputArray)):
        if inputArray[x] == elemToReplace:
            inputArray[x] = substitutionElem 
    return inputArray


print(arrayReplace([1,2,3,4,1,5],1,10))

# if x == elemToReplace