n = int(input())
for _ in range(n):
    dado = input()
    dado = [int(dado[0]), dado[1], int(dado[2])]
    if dado[0] == dado[2]:
        print(dado[0] * dado[2])
    elif dado[1].isupper():
        print(dado[2] - dado[0])
    else:
        print(dado[2] + dado[0])
