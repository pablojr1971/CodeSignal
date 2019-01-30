def arrayMaxConsecutiveSum(inputArray, k):
    c = sum(inputArray[:k])
    li=[c]
    while len(inputArray)>k:
        
        
        c = c +  inputArray[k] - inputArray[0] 
        li+=[c]
        del inputArray[0]

        
        

    
    return max(li)


print(arrayMaxConsecutiveSum([2,3,5,1,6],2))