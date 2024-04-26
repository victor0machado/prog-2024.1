n = int(input())
x = [int(i) for i in input().split()]

print(f"Menor valor: {min(x)}")
print(f"Posicao: {x.index(min(x))}")
