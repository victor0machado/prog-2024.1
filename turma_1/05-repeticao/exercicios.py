"""
Programação Estruturada
2024.1
18/03/2024

Estruturas de Repetição
Exercícios - nota de aula 07
"""

def conta_pares(min, max):
    """
    Elaborar uma função conta_pares(min, max) para exibir todos os valores
    entre min e max, inclusive, com um incremento de 2, separando-os com um
    hífen. Ex.: 2 - 4 - 6 - 8 - 10 - 12 - 14.
    """
    if min % 2:
        min += 1
    for num in range(min, max + 1, 2):
        if num >= max - 1:
            print(num)
        else:
            print(num, end=" - ")

conta_pares(2, 8) # 2 - 4 - 6 - 8
conta_pares(1, 9) # 2 - 4 - 6 - 8
conta_pares(1, 8) # 2 - 4 - 6 - 8
conta_pares(2, 9) # 2 - 4 - 6 - 8

def fatorial(num):
    """
    Faça um programa que calcule o fatorial de um número inteiro
    positivo fornecido pelo usuário.
    Ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120.
    """
    fat = 1
    for mult in range(1, num + 1):
        fat *= mult

    return fat

print(fatorial(1000))

def fatorial2(num):
    """
    Faça um programa que calcule o fatorial de um número inteiro
    positivo fornecido pelo usuário.
    Ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120.

    Solução por recursão.
    n! = n * (n - 1)!
    """
    if num == 1:
        return 1
    return num * fatorial2(num - 1)

print(fatorial2(5))
# print(fatorial2(1000)) -> sobe um erro de recursão
