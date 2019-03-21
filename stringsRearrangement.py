#from itertools import permutations
# >> > print permutations(['1', '2', '3'])
# <itertools.permutations object at 0x02A45210 >
# >> >
# >> > print list(permutations(['1', '2', '3']))


from itertools import permutations


def stringsRearrangement(inputArray):

    for per in permutations(inputArray):

        for tn in range(len(per)-1):
            count = 0

            for po in range(len(per[tn])):
                if per[tn][po] != per[tn+1][po]:
                    count += 1
            if count == 1:
                continue
            else:
                break
        else:  # only executed if the inner loop did NOT break
            return True

    return False

print(stringsRearrangement(["abc", "bac", "bbc", "bbe", "bbd"]))
#print(stringsRearrangement(["ab", "bb", "aa"]))
# If you're stuck, make sure ["abc","bac","bbc","bbe","bbd"] returns false.




# for x in xrange(10):
#     for y in xrange(10):
#         print x*y
#         if x*y > 50:
#             break
#     else:
#         continue  # only executed if the inner loop did NOT break
#     break  # only executed if the inner loop DID break
# The same works for deeper loops:

# for x in xrange(10):
#     for y in xrange(10):
#         for z in xrange(10):
#             print x,y,z
#             if x*y*z == 30:
#                 break
#         else:
#             continue
#         break
#     else:
#         continue
#     break


# Winner from CodeSignal


# from itertools import permutations

# def diff(w1, w2):
#     return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1

# def stringsRearrangement(inputArray):
#     for z in permutations(inputArray):
#         if sum([diff(*x) for x in zip(z, z[1:])]) == len(inputArray) - 1:
#             return True
#     return False
