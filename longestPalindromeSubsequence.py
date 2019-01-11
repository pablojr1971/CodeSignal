def longestPalindromeSubsequence(input):
    # freq = {}
    # for c in a:
    #     freq[c] = a.count(c)

    # a=[x for x in input if input.count(x)>=2 and x !=' ']
    a = [x for x in input if x != ' ']
    print(a)

    nl = []

    for c in a:
        pal = ''
        plen = 0

        if str(a).rfind(c) == str(a).index(c):
            if nl == []:
                pal = c

        else:
            pal=pal[:len(pal)//2] + c*2 + pal[(len(pal)//2+2):]
            
        
        nl.append(pal)

    print(nl)
    print(pal)
    print(plen)

    # return len([v for v in freq.values() if v % 2 != 0]) <= 1


# print(longestPalindromeSubsequence('ABCCBDDCE'))
print(longestPalindromeSubsequence('RECKLESS IS HE'))
