def r(x, y):
    return (3 * x) ** 2 + y ** 2

def b(x, y):
    return 2 * (x ** 2) + (5 * y) ** 2

def c(x, y):
    return -100 * x + y ** 3

n = int(input())
for _ in range(n):
    nums = [int(i) for i in input().split()]
    rafael = r(*nums)
    beto = b(*nums)
    carlos = c(*nums)
    if rafael > beto and rafael > carlos:
        print("Rafael ganhou")
    elif beto > rafael and beto > carlos:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")
