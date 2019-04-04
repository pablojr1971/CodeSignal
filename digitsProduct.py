def digitsProduct(product):
#     l = []
    if product==0:
        return 10
    if product==1:
        return 1

    
    r = []
    while product > 1:
        l = [x for x in range(9, 1, -1) if product % x == 0]
        if l==[]:
            return -1

        r += [str(l[0])]
        product = product/l[0]
    return int(''.join(r)[::-1])


print(digitsProduct(450))
print(digitsProduct(12))
print(digitsProduct(26))
print(digitsProduct(0))
print(digitsProduct(13))

def digitsProductWinner(p):
    if p == 0:
        return 10
    elif p == 1:
        return 1
    
    n = []

    while 1 < p:
        for d in range(9, 1, -1):
            if p % d == 0:
                p /= d
                n.append(d)
                break
        else:
            return -1

    return int(''.join(map(str, sorted(n))))
