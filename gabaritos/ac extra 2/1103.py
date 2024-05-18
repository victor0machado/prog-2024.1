while True:
    h1, m1, h2, m2 = [int(i) for i in input().split()]

    if h1 == m1 == h2 == m2 == 0:
        break

    minutos_1 = h1 * 60 + m1
    minutos_2 = h2 * 60 + m2

    minutos = minutos_2 - minutos_1
    if minutos < 0:
        minutos += 24 * 60

    print(minutos)
