import numpy as np


def mine(image):
    m = np.array(image)
    k = np.empty_like(m, dtype=int)
 

    res=np.insert(m, 0, False, axis=1)
    res=np.insert(res, len(res[0, :]), False, axis=1)
    res=np.insert(res, 0, False, axis=0)
    res=np.insert(res, len(res[:, 0]), False, axis=0)


    it = np.nditer(m, flags=['multi_index'])
    while not it.finished:
        
        mrow=it.multi_index[0]+1
        mcol=it.multi_index[1]+1
        

        
        nbombs=sum(list([sum(res[mrow-1, mcol-1:mcol+2]),res[mrow][mcol-1],res[mrow][mcol+1],sum(res[mrow+1, mcol-1:mcol+2])]))
        k[it.multi_index[0]][it.multi_index[1]]=nbombs
                      
        it.iternext()



    return k


# print(mine(image=[[7, 4, 0, 1],
#                   [5, 6, 2, 2],
#                   [6, 10, 7, 8],
#                   [1, 4, 2, 0]]))

print(mine(image=[[True, False, True],
                   [False, False, False],
                   [True, False, False]]))



