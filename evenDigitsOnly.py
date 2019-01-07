def evenDigitsOnly(n):
    s = str(n)
    for x in s:
        if int(x) % 2 != 0:
            return False
    return True


print(evenDigitsOnly(426))


def evenDigitsOnly_winner(n):
    return all([int(i)%2==0 for i in str(n)])