import string
def isBeautifulString(inputString):
    
    # d=((ord(i),inputString.count(i)) for i in inputString)
    # # d=list(d)
    # # for c in d.items():
    # #     print(c)

    # # for c in d.keys():
    # #     print(c)
    # # new=(sorted(d.items(), key=lambda x: (x[1],x[0]), reverse=True))
    # # print(new)
    # # print(len(d))
    # # print(new[-1])
    # # if new[-1][0] - len(new) + 1 ==97:
    # if d[-1][0] - len(d) + 1 ==97:
    #     return True
    # else:
    #     return False
    # # return (sorted(inputString))



    r = [inputString.count(i) for i in string.ascii_lowercase]
    
    return r[::-1] == sorted(r)

#print(isBeautifulString('aaabbbbccca'))
print(isBeautifulString('aabbb'))
#print(isBeautifulString('abcdefghijklmnopqrstuvwxyzqwertuiopasdfghjklxcvbnm'))
# print(isBeautifulString("bbbaacdafe"))