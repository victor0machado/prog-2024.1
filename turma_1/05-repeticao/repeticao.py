"""
Programação Estruturada
2024.1
18/03/2024

Estruturas de Repetição
- while -> quando não sabemos quantas vezes vamos executar a
repetição
- for -> quando queremos acessar todos os elementos de uma
coleção de dados
"""

def contagem_regressiva(num):
    while num >= 0:
        print(num)
        num -= 1 # num = num - 1

    print("acabou")

contagem_regressiva(5)

# range([start], stop, [step])
# start - inclusive
# stop - exclusive
# step - passo

print(list(range(5)))        # 0, 1, 2, 3, 4
print(list(range(2, 5)))     # 2, 3, 4
print(list(range(2, 10, 3))) # 2, 5, 8
print(list(range(10, -5, 2)))

def contagem_regressiva2(num):
    for cont in range(num, -1, -1): # 5, 4, 3, 2, 1, 0
        print(cont)

contagem_regressiva2(5)

def ola_varias_vezes(n):
    # caractere curinga
    for _ in range(n):
        print("olá")

ola_varias_vezes(3)

def pula_mult_3(maximo):
    for x in range(1, maximo + 1):
        if x % 3 == 0:
            continue # pula para a próxima iteração
        print(x)

pula_mult_3(10)

def para_antes_de_10(maximo):
    for x in range(1, maximo + 1):
        if x >= 10:
            break # interrompe por completo a estrutura de rep.
        print(x)

    print("acabou")

print("-" * 30)
para_antes_de_10(5)

def e_primo(num):
    for div in range(2, num): # 2, 3, 4, 5, 6
        if num % div == 0:
            print(num, "não é primo.")
            break
    else:
        print(num, "é primo.")

e_primo(7)
e_primo(11)
e_primo(2)
e_primo(35)
