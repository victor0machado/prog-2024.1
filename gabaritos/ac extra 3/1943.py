k = int(input())

posicoes = [1, 3, 5, 10, 25, 50, 100]
for posicao in posicoes:
    if k <= posicao:
        print("Top", posicao)
        break
