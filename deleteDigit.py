def deleteDigit(n):
    l=[]
    for x in str(n):
        s=str(n).replace(x,'',1)
        l+=[int(s)]
    return max(l)
    
print(deleteDigit(222219))