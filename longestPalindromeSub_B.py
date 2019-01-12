def longestPalindromeSubsequence(input):
    a = input.replace(" ", "")
    print(a)
    nl = []

    for c in a:
        first_c = a.index(c)
        last_c = a.rfind(c)

        def recur(pal):
            if len(pal) == 1:
                return pal

            if len(pal) == 2:
                if pal[0] != pal[1]:
                    return pal[0]
                else:
                    return pal

            else:
                nl.append(a[first_c] + recur(
                    a[first_c+1:last_c]) + a[last_c])

        if first_c == last_c:  # unique character
            if nl == []:
                nl.append(c)
        else:
            recur(a[first_c:last_c])

            # # while len(a) > 0:
            # #     pal_recursive(a)
            # #     a = a[1:]
            # pal_recursive(a)
    print(nl)


# print(longestPalindromeSubsequence('ABCCBDDCE'))
print(longestPalindromeSubsequence('REESS IS HE'))
#print(longestPalindromeSubsequence('PAB AAB R'))
