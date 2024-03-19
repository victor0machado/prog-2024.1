n = int(input())

for _ in range(n):
    entrada = input()
    extracao = []
    diamantes = 0
    for char in entrada:
        if char == ".":
            continue
        if char == "<":
            extracao.append(char)
        else:
            if len(extracao) >= 1 and extracao[-1] == "<":
                extracao.pop()
                diamantes += 1

    print(diamantes)
