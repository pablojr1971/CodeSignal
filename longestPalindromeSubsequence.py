def longestPalindromeSubsequence(input):
    a = input.replace(" ", "")
    print(a)
    nl = []

    def pal_recursive(accumulated_pal):

        # Base case
        # Return the final state
        if len(accumulated_pal) == 0:
            return ""

        if len(accumulated_pal) == 1:
            return accumulated_pal

        if len(accumulated_pal) == 2:
            if accumulated_pal[0] != accumulated_pal[1]:
                return accumulated_pal[0]
            else:
                return accumulated_pal

        # Recursive case
        cha = accumulated_pal[0]
        first_c = 0  # accumulated_pal.index(cha)
        last_c = accumulated_pal.rfind(cha)

        if first_c == last_c:  # unique character
            if nl == []:
                nl.append(cha)

            # accumulated_pal = accumulated_pal[1:]
            # pal_recursive(accumulated_pal[1:])
            first_c += 1

        nl.append(accumulated_pal[first_c] + pal_recursive(
            accumulated_pal[first_c+1:last_c]) + accumulated_pal[last_c])

    # while len(a) > 0:
    #     pal_recursive(a)
    #     a = a[1:]
    pal_recursive(a)
    print(nl)


# print(longestPalindromeSubsequence('ABCCBDDCE'))
#print(longestPalindromeSubsequence('REESS IS HE'))
print(longestPalindromeSubsequence('PAB AAB R'))
