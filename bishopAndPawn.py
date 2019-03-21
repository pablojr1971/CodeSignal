def bishopAndPawn(b, pawn):
    li = []

    for a in range(7):
        li += [chr(ord(b[0])+a+1) + str(int(b[1])+a+1)]
        li += [chr(ord(b[0])+a+1) + str(int(b[1])-a-1)]
        li += [chr(ord(b[0])-a-1) + str(int(b[1])+a+1)]
        li += [chr(ord(b[0])-a-1) + str(int(b[1])-a-1)]

    return pawn in li


print(bishopAndPawn("H1", "D6"))
