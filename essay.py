# listA = [0]
# listB = listA
# listB.append(1)
# print(listA)
# print(listB)



list1 = [0, 1, 2, 3, 4]
list2 = list1[:]
list3 = list1
name1 = 10
name2 = 10

list1[1] = 35

print(list1)
print(list2)
print(id(list1))
print(id(list2))
print(id(list3))
print(type(list1))
print(type(list2))
print(type(list3))

print(id(name1))
print(type(name1))
print(id(name2))
print(type(name2))

list1.sort()
print(list1)
