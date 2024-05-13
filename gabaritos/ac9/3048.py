n = int(input())
numeros = []
for _ in range(n):
    numeros.append(int(input()))

cont = 1
for i in range(0, len(numeros) - 1):
    if numeros[i] != numeros[i + 1]:
        cont += 1

print(cont)
