def maior(a, b):
    return a if a > b else b

dados = input().split(" ")

maximo = maior(maior(int(dados[0]), int(dados[1])), int(dados[2]))
print(maximo, "eh o maior")
