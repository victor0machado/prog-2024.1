n = int(input())
dist = 0
for _ in range(n):
    t, v = [int(i) for i in input().split()]
    dist += t * v

print(dist)
