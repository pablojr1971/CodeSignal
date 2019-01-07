def areSimilar(a, b):

    # return len([(x, y)for x, y in zip(a, b) if x != y]) <= 2 and (len(set(a+b)) == len(a))  fails secret tests
    return len([(x, y)for x, y in zip(a, b) if x != y]) <= 2 and sorted(a) == sorted(b)


#print(areSimilar([1, 1, 4], [1, 2, 3]))
print(areSimilar([4, 6, 3], [6, 4, 3]))
