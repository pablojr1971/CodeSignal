def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):

    my = [yourLeft, yourRight]
    friend = [friendsLeft, friendsRight]
    if max(my) == max(friend) and yourLeft + yourRight == friendsLeft + friendsRight:
        return True
    return False


print(areEquallyStrong(20, 15, 10, 25))

# def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
#     return {yourLeft, yourRight} == {friendsLeft, friendsRight}
