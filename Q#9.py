#Question No. 9
#Ankit Mittal

PERIMETER = 1000
for a in range(1, PERIMETER + 1):
    for b in range(a + 1, PERIMETER + 1):
            c = PERIMETER - a - b
            if a * a + b * b == c * c:
                    # It is now implied that b < c, because we have a > 0
                    print str(a * b * c)
