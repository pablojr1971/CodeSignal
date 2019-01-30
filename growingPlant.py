def growingPlant(upSpeed, downSpeed, desiredHeight):
    days = 1
    height = 0

    while height + upSpeed < desiredHeight:
        height = height+upSpeed - downSpeed
        days+=1
    return days


print(growingPlant(10, 9, 4))
