def dias(peso):
    d = 0
    while peso > 1:
        d += 1
        peso /= 2

    return d

n = int(input())
for _ in range(n):
    peso = float(input())
    print(dias(peso), "dias")
