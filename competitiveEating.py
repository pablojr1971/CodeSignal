def competitiveEating(t, width, precision):
    return '{: ^{width}.{precision}}'.format(t,width=width,precision=precision)


def competitiveEating_Winner(t, width, precision):
    return ('{:^{w}.{p}f}').format(t,w=width,p=precision)

print(competitiveEating_Winner(0,50,5))