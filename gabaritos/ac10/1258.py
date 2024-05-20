primeira_vez = True
while True:
    n = int(input())
    if n == 0:
        break

    if not primeira_vez:
        print()
    primeira_vez = False

    dados = []
    for _ in range(n):
        nome = input()
        cor, tamanho = input().split()
        dados.append([nome, cor, tamanho])

    for cor in ["branco", "vermelho"]:
        for tamanho in ["P", "M", "G"]:
            nomes = [dado[0] for dado in dados if dado[1] == cor and dado[2] == tamanho]
            nomes.sort()
            for nome in nomes:
                print(cor, tamanho, nome)
