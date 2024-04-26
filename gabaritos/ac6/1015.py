def dist(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

p1 = input().split(" ")
p2 = input().split(" ")

distancia = dist(float(p1[0]), float(p1[1]), float(p2[0]), float(p2[1]))
print(f"{distancia:.4f}")
