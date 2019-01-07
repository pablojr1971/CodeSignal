def arrayMaximalAdjacentDifference(inp):
    counter = 0
    for a in range(len(inp)-1):
        if abs(inp[a+1]-inp[a]) > counter:
            counter = abs(inp[a+1]-inp[a])
        else:
            continue

    return counter


print(arrayMaximalAdjacentDifference([1, -44, 5, 9]))


def arrayMaximalAdjacentDifference_Winner(a):
    diffs = [abs(a[i]-a[i+1]) for i in range(len(a)-1)]
    return max(diffs)
