import ipaddress


def isIPv4Address(s):

   # return len([a for a in s.split(".") if (str.isdigit(a) and int(a) in list(range(256)))]) == 4

    for a in s.split("."):
        if a != "" and str.isdigit(a) and int(a) in list(range(256)):
            continue
        else:
            return False

    return len(s.split(".")) == 4


print(isIPv4Address('172..1.2.4'))


def isIPv4Address_Winner(s):
    p = s.split('.')

    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)


def isIPv4Address_another(inputString):
    try:
        ipaddress.ip_address(inputString)
    except:
        return False
    return True
