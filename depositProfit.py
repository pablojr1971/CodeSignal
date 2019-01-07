def depositProfit(deposit, rate, threshold):
    counter=0
    while deposit < threshold:
        deposit=deposit*(1+(rate/100))
        counter+=1

    return counter



print(depositProfit(100, 20, 170))
