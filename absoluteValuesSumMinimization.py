def absoluteValuesSumMinimization(a):
    #return min([abs(p - x) for p in a for x in a])
    ls=[]
    for x in a:
        count=0
        for p in a:
            count+=abs(p-x)
        ls.append((x,count))
    d=dict(ls)
    return min(d, key=d.get)
print(absoluteValuesSumMinimization([ 2, 4, 7]))
