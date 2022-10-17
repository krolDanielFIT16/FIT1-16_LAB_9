def getArea(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


triangles = {
    "A": (5, 6, 7),
    "B": (8, 9, 5),
    "C": (4, 3, 2)
}

res = {}

for key in triangles.keys():
    S = getArea(*triangles[key])
    res[key] = S

print(triangles)
print(res)
print()

m = max(res, key=res.get)
print(f"{m}, {triangles[m]}, S = {res[m]}")
