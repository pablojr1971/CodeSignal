import string


def longestWord(s):
    l = []
    w = ''
    for a in range(len(s)):
        if s[a] in string.ascii_letters:
            w += s[a]
        else:
            if w == '':
                continue
            else:
                l += [w]
                w = ''
    l += [w]
    return max(l, key=len)

import re
def longestWord_Winner(text):
    words=re.findall(r'[a-zA-Z]+',text)
    return max(words,key=len)


print(longestWord('!!! Phrase one!'))
