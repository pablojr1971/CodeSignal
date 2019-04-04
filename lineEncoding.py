def lineEncoding(r):
    s = ''
    l = []
    
    for n in range(len(r)-1):
        if r[n+1] == r[n]:
            continue
        else:
            l += [str(n+1)+r[n]]
    if len(r) != l[-1][0]:
        l += [str(len(r))+r[-1]]

    for x in l[-1:0:-1]:
        
        print(x)

    # for x in l:
    #     s=''.join

    print(l)
    return s

print(lineEncoding('aaabbaaa'))
