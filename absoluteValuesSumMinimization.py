def absoluteValuesSumMinimization(a):
    return min([abs(p - x) for p in a for x in a])


print(absoluteValuesSumMinimization([ 2, 4, 7]))
