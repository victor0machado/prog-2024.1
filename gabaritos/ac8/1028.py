def mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a

n = int(input())
for _ in range(n):
    nums = [int(i) for i in input().split()]
    print(mdc(*nums))
