import re


def reverseParentheses(s):
    pablo_Regex = re.compile(r'\(([^()]+)\)')  # borrowed
    mo = pablo_Regex.search(s)

    while mo != None:
        s = s.replace(mo.group(0), mo.group(0)[1:-1][::-1])
        mo = pablo_Regex.search(s)

    return s


print(reverseParentheses('The ((quick nworb xof jumps over the lazy) dog)'))
