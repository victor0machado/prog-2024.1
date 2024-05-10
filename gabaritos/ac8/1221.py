def e_primo(num):
    div = 2
    while div * div <= num:
        if num % div == 0:
            print("Not Prime")
            return

        div += 1

    print("Prime")


n = int(input())
for _ in range(n):
    numero = int(input())
    e_primo(numero)
