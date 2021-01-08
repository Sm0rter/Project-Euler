notfound = True

for a in range(1000):
    print(a)
    for b in range(1000):
        if a + b > 1000:
            pass
        if a >= b:
            pass
        c = 1000 - a - b
        if b >= c or a >= c:
            pass
        if a + b + c == 1000:
            if a**2 + b**2 == c**2:
                if a != b and b != c and a != c:
                    notfound = False
                    goodlist = [a,b,c]
print(goodlist)
print(goodlist[0]*goodlist[1]*goodlist[2])