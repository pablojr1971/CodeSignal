def alphabeticShift(inputString):
    res=''
    

    for x in range(len(inputString)):
        if inputString[x]=='z':
            res += 'a'
            continue

        res += chr(ord(inputString[x]) + 1)

    return res


print(alphabeticShift('z'))
