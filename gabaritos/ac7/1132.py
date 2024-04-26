x = int(input())
y = int(input())

if x > y:
    x, y = y, x

soma = 0
for num in range(x, y + 1):
    if num % 13:
        soma += num

print(soma)
