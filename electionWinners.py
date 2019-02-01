def electionsWinners(votes, k):
    return len([x for x in votes if x+k > max(votes)])
    

#print(electionsWinners([2, 3, 5, 2],3))
print(electionsWinners([5, 1, 3, 4, 1],0))
