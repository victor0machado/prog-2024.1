n = int(input())
numeros = [int(input()) for _ in range(n)]

pares = [i for i in numeros if i % 2 == 0]
impares = [i for i in numeros if i % 2 == 1]

pares.sort()
impares.sort(reverse=True)

for num in pares + impares:
    print(num)
