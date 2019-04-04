def electionsWinners(votes, k):
    if k==0:
        li=[x for x in votes if x==max(votes)]
        return 1 if len(li)==1 else 0
    else:
        li=[x for x in votes if x+k>max(votes)]
        return len(li)
    


        # print(a)

print(electionsWinners([2, 3, 5, 2],3))
print(electionsWinners([5, 1, 3, 4, 1],0))
