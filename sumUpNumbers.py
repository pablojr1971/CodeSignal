import re


def sumUpNumbers(inputString):
    numbers = re.findall(r'[0-9]+', inputString)
    numbers = [int(x) for x in numbers]
    return sum(numbers)


print(sumUpNumbers("45 oranges 6 pears, 7"))
