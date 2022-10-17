def getMultiples(m, count):
    for i in range(count):
        yield i*m


A = set(getMultiples(2, 100))
B = set(getMultiples(3, 100))
C = set(getMultiples(5, 100))

ALL = (A.union(B)).union(C)

print(1, set(filter(lambda x: x % 30 == 0, ALL)))
print(2, set(filter(lambda x: (x % 15 == 0 and x % 2 != 0), ALL)))
print(3, set(filter(lambda x: (x % 5 == 0 and (x % 2 != 0 and x % 3 != 0)), ALL)))
