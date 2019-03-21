def longestPalindromeSubsequence(input):
    a = input.replace(" ", "")
    nl = []

    def check_longest(be):  # a function to obtain the longest distance between 2 same characters
        li = []
        for c in be:
            first = be.index(c)
            last = be.rfind(c)
            li.append(be[first:last+1])
        return max(li, key=len)

    def form_pal(accu):
        if len(accu) == 1:
            return accu
        if len(accu) == 2:
            if accu[0] != accu[1]:
                return accu[0]
            else:
                return accu
        else:
            return accu[0] + form_pal(check_longest(accu[1:-1])) + accu[-1]

    # while len(a) > 0:
    #     for sub in range(len(a)):
    #         nl.append(form_pal(check_longest(a[:sub+1])))
    #     a = a[1:]

    nl.append(form_pal(check_longest(a)))
    return max(nl, key=len)


print(longestPalindromeSubsequence("AN ELEGANT WEAPON"))
# ANELENA
