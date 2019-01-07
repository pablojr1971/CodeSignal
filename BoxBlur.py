import numpy as np


def boxBlur(image):
    m = np.array(image)
    result = np.empty([len(m[:, 0])-2,len(m[0, :])-2], dtype = int) 
    for row in range(len(m[:, 0])-2):
        for col in range(len(m[0, :])-2):
            #print(row, col)
            a = int((sum(sum(m[row:row+3, col:col+3])))/9)
            # print(m[row:row+3, col:col+3])
            # print(a)
            result[row,col]=a
    return result


print(boxBlur(image=[[7, 4, 0, 1],
                     [5, 6, 2, 2],
                     [6, 10, 7, 8],
                     [1, 4, 2, 0]]))
