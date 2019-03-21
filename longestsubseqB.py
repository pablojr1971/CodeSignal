def longestPalindromeSubsequence(i):
    return r(i.replace(' ', ''))


def r(i):
    p = []
    while i:
        n, i = i[0], i[1:]
        b = i.rfind(n)
        if b >= 0:
            n += r(i[:b]) + n
        p += [n]
    return max(p, key=len) if p else ''


# print(longestPalindromeSubsequence("AN ELEGANT WEAPON"))
print(longestPalindromeSubsequence("ne1len"))
