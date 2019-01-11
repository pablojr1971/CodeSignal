def palindromeRearranging(a):
    # a = sorted(a)
    # if a[0] != a[1] and a[1::2] == a[2::2]:
    #     return True
    # elif a[0::2] == a[1::2]:
    #     return True

    freq = {}
    for c in a:
        freq[c] = a.count(c)

    return len([v for v in freq.values() if v % 2 != 0]) <= 1


print(palindromeRearranging("cccaaa"))


# def palindromeRearranging(inputString):

#     return sum([inputString.count(i) % 2 for i in set(inputString)]) <= 1
