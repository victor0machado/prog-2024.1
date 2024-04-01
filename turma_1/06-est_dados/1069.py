n = int(input())

for _ in range(n):
    escavacao = input()
    diamantes = 0
    pilha = []
    for retirada in escavacao:
        if retirada == ".":
            continue
        if retirada == "<":
            pilha.append(retirada)
        else:
            if len(pilha) > 0 and pilha[-1] == "<":
                pilha.pop()
                diamantes += 1
            else:
                pilha.append(">")
    print(diamantes)
