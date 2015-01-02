#map/reduce excersised
def f1(s):
    capstr = ''
    for x in s[1:]:
        capstr = capstr + x.lower()
    return s[0].upper()+capstr

f = map(f1,['adam', 'LISA', 'barT'])
print f
