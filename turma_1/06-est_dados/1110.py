while True:
    n = int(input())
    if n == 0:
        break

    cartas = [num for num in range(n, 0, -1)]
    descartadas = []

    while len(cartas) >= 2:
        descartadas.append(cartas.pop())
        cartas.insert(0, cartas.pop())

    descartadas = [str(num) for num in descartadas]
    print("Discarded cards:", ", ".join(descartadas))
    print("Remaining card:", cartas[0])
