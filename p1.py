planets = ("Меркурий", "Венера", "Земля", "Марс", "Юпитер", "Сатурн", "Уран", "Нептун")
iters = int(input("> "))
si = iters
i = 0
while iters > 0:
    print(si-iters, planets[i])
    iters -= 1
    i += 1
    if i >= len(planets):
        i = 0
