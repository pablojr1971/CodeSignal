def isBeautifulString(inputString):
    
    d={ord(i):inputString.count(i) for i in inputString}
    for c in d.items():
        print(c)
    # return (sorted(inputString))

print(isBeautifulString('aaabbbbccca'))