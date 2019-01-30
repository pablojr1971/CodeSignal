def knapsackLight(value1, weight1, value2, weight2, maxW):
    li=[0]
    if weight1 + weight2 <= maxW:
        li+=[value1 + value2]
        
    if weight1  <= maxW:
        li+=[value1]

    if weight2  <= maxW:
        li+=[value2]

    return max(li)


print(knapsackLight(10,2,11,3,1))