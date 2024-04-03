def distancia(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

a = [float(x) for x in input().split(" ")]
b = [float(x) for x in input().split(" ")]

print(f"{distancia(a, b):.4f}")
