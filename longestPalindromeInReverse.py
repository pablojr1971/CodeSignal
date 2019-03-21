def longestPalindromeInReverse(i):
    return r(i.replace(' ', ''))


def r(i):
    p = []
    for a in range(len(i)):
        if isPalindrome(i[-(a+1):]):
            p += [i[-(a+1):]]
    # return max(p, key=len) if p else ''
    #s3 = s1[len(s2):]
    i = i + i[:-len(max(p, key=len)):][::-1]
    return i


def isPalindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])


print(longestPalindromeInReverse("apcdcq"))


# print(isPalindrome('uli')) bcdcb
