while True:
    k = int(input())
    if k == 0:
        break

    n, m = [int(i) for i in input().split()]
    for _ in range(k):
        x, y = [int(i) for i in input().split()]
        if x == n or y == m:
            print("divisa")
        elif x > n and y > m:
            print("NE")
        elif x > n and y < m:
            print("SE")
        elif x < n and y > m:
            print("NO")
        else:
            print("SO")
