def circleOfNumbers(n, firstNumber):
    if firstNumber >= n/2:
        return firstNumber - n/2
    else:
        return firstNumber + n/2


print(circleOfNumbers(8, 3))

def circleOfNumbers_better(n, f):
    return f-n/2 if (f-n/2)>=0 else (f-n/2)+n