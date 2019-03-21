# def digitDegreeold(n):

#     def recur(s, c=0):
#         res = 0

#         if len(s) == 1:
#             return c

#         for a in s:
#             res += int(a)

#         recur(str(res), c+1)

#     recur(str(n), c=0)


# print(digitDegree(91))


def digitDegree(n, c=0):

    res = 0

    if len(str(n)) == 1:
        return c

    else:
        for a in str(n):
            res += int(a)

        return digitDegree(res, c+1)


print(digitDegree(91))


# def digitDegree(n,i=0):
#     n=str(n)
#     if len(n)==1:
#         return i
#     else:
#         return digitDegree(sum((int(x) for x in n)),i+1)
