n = int(input())

for _ in range(n):
    compras = list(set(input().split(" ")))
    compras.sort()
    print(" ".join(compras))
