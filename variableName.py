import re


def variableName(s):
    p = re.compile(r'\w+') 
    mo = p.search(s)

    p1 = re.compile(r'^[^0-9]') 
    mo1 = p1.search(s)
    

    return mo != None and mo1 != None \
            and len(mo.group()) == len(s)


print(variableName('_5'))


#Winner
def variableName(name):

    if re.match('[a-z_][0-9_a-z]*$', name,re.IGNORECASE):
        return True
    return False