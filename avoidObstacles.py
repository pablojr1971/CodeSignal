def avoidObstacles(a):

    for target in range(2, max(a)+2):
        li = [b for b in a if b % target == 0]
        if len(li) != 0:
            continue
        break
    return target


print(avoidObstacles([999, 1000]))
