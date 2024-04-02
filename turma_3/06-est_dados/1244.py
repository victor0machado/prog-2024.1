n = int(input())

for _ in range(n):
    entrada = input()
    palavras = entrada.split(" ")

    palavras.sort(key=len, reverse=True)
    print(" ".join(palavras))
