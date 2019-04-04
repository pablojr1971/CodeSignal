def constructShell(n):
    return [[0]*(i+1) if i <= n-1 else [0] * ((2*n)-i-1) for i in range((2*n)-1)]


print(constructShell(9))
