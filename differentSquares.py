def differentSquares(matrix):
    l=[]
    for row in range(len(matrix)-1):
        for col in range(len(matrix[0])-1):
            sq=str(matrix[row][col])+str(matrix[row][col+1])+str(matrix[row+1][col])+str(matrix[row+1][col+1])
            l+=[sq]
    return (len(set(l)))       


print(differentSquares([[2, 5, 3, 4, 3, 1, 3, 2],
                        [4, 5, 4, 1, 2, 4, 1, 3],
                        [1, 1, 2, 1, 4, 1, 1, 5],
                        [1, 3, 4, 2, 3, 4, 2, 4],
                        [1, 5, 5, 2, 1, 3, 1, 1],
                        [1, 2, 3, 3, 5, 1, 2, 4],
                        [3, 1, 4, 4, 4, 1, 5, 5],
                        [5, 1, 3, 3, 1, 5, 3, 5],
                        [5, 4, 4, 3, 5, 4, 4, 4]]))
