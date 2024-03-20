while True:
    n = int(input())
    if n == 0:
        break

    lista = list(range(n, 0, -1))
    descartados = []
    while len(lista) > 1:
        descartados.append(lista.pop())
        lista.insert(0, lista.pop())

    descartados = [str(num) for num in descartados]
    print("Discarded cards:", ", ".join(descartados))
    print("Remaining card:", lista[0])
