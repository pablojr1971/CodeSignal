def arrayChange(a):
    b = a[:]
    for i in range(len(a)-1):
        if a[i+1] > a[i]:
            continue
        elif a[i+1] == a[i]:
            a[i+1] += 1
            continue
        a[i+1] = a[i]+1

    print(a)
    print(b)
    return sum(a) - sum(b)


print(arrayChange([-1000, 0, -2, 0]))
