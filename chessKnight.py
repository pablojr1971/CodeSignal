def chessKnight(cell):
    
    moves=8
    col=ord(cell[0])-96
    row=int(cell[1])

    if col in [2,7] and row in range(3,7): moves-=2
    if row in [2,7] and col in range(3,7): moves-=2

    if col in [1,8] and row in range(3,7): moves-=4
    if row in [1,8] and col in range(3,7): moves-=4

    if col in [2,7] and row in [2,7]: moves-=4

    if col in [2,7] and row in [1,8]: moves-=5
    if col in [1,8] and row in [2,7]: moves-=5
    
    if col in [1,8] and row in [1,8]: moves-=6


    return moves
    
    # print(str(col)+str(row))
    # print(moves)
        

def chessKnight_Winner(cell):

    row = ord(cell[0]) - ord('a')
    col = int(cell[1]) - 1
    
    count = lambda i, j : 1 if (0 <= i < 8) and (0 <= j < 8) else 0
    
    moves = ((1,2), (-1,2), (1,-2), (-1, -2), (2,1), (-2, 1), (2, -1), (-2, -1))
    
    return sum(count(row + move[0], col + move[1]) for move in moves)

print(chessKnight('h8'))