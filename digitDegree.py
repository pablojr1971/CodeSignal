

def digitDegree(n):
    res=n
    c=0
    

    def recur(s,c):
        global res
        if len(s)==1:
            return c

        for a in s:
            res+=int(a)
        c+=1

    recur(str(res),c)
    

print(digitDegree(91))
