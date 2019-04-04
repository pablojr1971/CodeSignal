def validTime(time):
    return 0 <= int(time[:2]) <= 11 and 0 <= int(time[3:]) <= 59


print(validTime("00:70"))
