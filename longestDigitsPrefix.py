def longestDigitsPrefix(inputString):
    li=[]
   

    for a in inputString:
        if not a.isdigit():
            break

        li+=a

    return ''.join(li)    



print(longestDigitsPrefix('0123456789'))