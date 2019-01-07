import itertools


def alternatingSums(a):

    firstcolumn = 0
    secondcolumn = 0
    # zip will stop on the shortest seq
    for x, y in itertools.zip_longest(a[::2], a[1::2]):
        firstcolumn += x
        if y != None:
            secondcolumn += y
    return [firstcolumn, secondcolumn]


print(alternatingSums([1, 2, 4, 5, 6, 7]))


# def alternatingSums(a):

#     return [sum(a[::2]),sum(a[1::2])]
