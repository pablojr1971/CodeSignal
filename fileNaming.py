def fileNaming(names):
    # for a in names:
    # l=[names.index(a) for a in names if names.count(a)>1]
            # for x in range(names.count(a)-1):
            #     names[x+1]+='('+str(x+1)+')'

    # l = []
    d = {i: v for i, v in enumerate(names)}
    n = d.copy()
    # n.clear()


    # for key, value in d.items():
    #     if vals.count(value) > 1:
    #         l += [key]

    for key in n.keys():
        n[key]=None

    # vals = list(n.values())

    for key, value in n.items():
        if d[key] not in n.values():
            n[key]=d[key]
        # else:
            # l=[key for   value ]
            #     names[x+1]+='('+str(x+1)+')'

    # print(l)
    print(d)
    print(n)



def fileNaming_winner(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            j=1
            while names[i]+"("+str(j)+")" in names[:i]:
                j+=1
            names[i]+="("+str(j)+")"
    return names

print(fileNaming_winner(["doc", "doc", "image", "doc(1)", "doc"]))

# ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]


# Input:
# names: ["dd",
#  "dd(1)",
#  "dd(2)",
#  "dd",
#  "dd(1)",
#  "dd(1)(2)",
#  "dd(1)(1)",
#  "dd",
#  "dd(1)"]
# Expected Output:
# ["dd",
#  "dd(1)",
#  "dd(2)",
#  "dd(3)",
#  "dd(1)(1)",
#  "dd(1)(2)",
#  "dd(1)(1)(1)",
#  "dd(4)",
#  "dd(1)(3)"]
