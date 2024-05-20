try:
    while True:
        n = int(input())
        h, c, l = [int(i) for i in input().split()]

        hip = (h ** 2 + c ** 2) ** 0.5
        area = n * hip * l / 10000

        print(f"{area:.4f}")
except EOFError:
    pass
