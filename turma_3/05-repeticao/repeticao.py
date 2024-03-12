"""
Programação Estruturada
2024.1
12/03/2024

Estruturas de repetição
- while (quando não temos certeza do número de operações)
- for   (quando o número de repetições é previsível)
"""

# while
def contagem_regressiva(num):
    while num >= 0:
        print(num)
        num -= 1 # num = num - 1

    print("acabou")

# Loop infinito - cuidado!
def contagem_regressiva2(num):
    while num >= 0:
        print(num)

    print("acabou")

contagem_regressiva(5)

# range
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))
print(list(range(-10, 2, 3)))
print(list(range(5, -15, -2)))
print(list(range(-5, 15, -2)))

# for
def contagem_regressiva3(num):
    for cont in range(num, -1, -1):
        print(cont)

    print(cont)

print("-" * 30)
contagem_regressiva3(5)

# quando eu não preciso do elemento que está na coleção iterada:
def ola_varias_vezes(num_vezes):
    for _ in range(num_vezes):
        print("olá")

print("-" * 30)
ola_varias_vezes(10)

# quando eu quero pular uma iteração:
def pi(num):
    for passo in range(1, num + 1):
        if not passo % 3:
            continue # pula para a próxima iteração
        print(passo)

print("-" * 30)
pi(15)

# quando eu quero interromper uma estrutura de repetição:
def le_nome():
    while True:
        nome = input("Informe o seu nome: ")
        if nome:
            break # sai por completo da estrutura de repetição

    print("Olá,", nome)

print("-" * 30)
# le_nome()

def teste():
    num = 0
    while num >= 0:
        for cont in range(15):
            print(cont)
            if cont == 5:
                break

        num = int(input("Informe um número: "))

# teste()

# else (é necessário usar o break)
def e_primo(num):
    for div in range(2, num):
        if not num % div:
            print(num, "é divisível por", div)
            print(num, "não é primo.")
            break
    else: # só entra se não tiver rodado o break
        print(num, "é primo.")

e_primo(6)
e_primo(7)
e_primo(31)
e_primo(49)
