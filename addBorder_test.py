def addBorder(picture):
    picture = ["*"*(len(picture[0])+2)] + picture
    picture = picture + ["*"*(len(picture[0]))]
    for i in range(1, len(picture)-1):
        picture[i] = "*" + picture[i] + "*"

    return picture


print(addBorder(["abc",
                 "ded"]))


# def addBorder(picture):

#     r = ['*'*(len(picture[0])+2)]
#     for i in picture:
#         r.append('*' + i + '*')

#     r.append(r[0])


#     return r
