dim_matriz = 12

c = int(input())
t = input()

resultado = 0
for i in range(dim_matriz ** 2):
    if i % dim_matriz == c:
        resultado += float(input())
    else:
        input()

if t == "M":
    resultado /= dim_matriz

print(f"{resultado:.1f}")
