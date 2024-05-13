n = int(input())

for _ in range(n):
    m = int(input())
    frutas = {}
    for _ in range(m):
        dados = input().split()
        frutas[dados[0]] = float(dados[1])

    p = int(input())
    valor = 0
    for _ in range(p):
        dados = input().split()
        valor += frutas[dados[0]] * int(dados[1])

    print(f"R$ {valor:.2f}")
