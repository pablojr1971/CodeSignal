import string
def isMAC48Address(inputString):
    for a in inputString.split('-',5):
        if len(a)!=2: return False
        for x in a:
            if x not in '0123456789ABCDEF':
                return False

    return True

print(isMAC48Address("Z1-1B-63-84-45-E6"))
print(isMAC48Address("00-1c-63-84-45-E6"))
print(isMAC48Address("02-03-04-05-06-07-"))