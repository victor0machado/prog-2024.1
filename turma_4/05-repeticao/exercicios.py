"""
Programação Estruturada
2024.1
15/03/2024

Estruturas de Repetição
Exercícios - Nota de aula 07
"""

def conta_pares(min, max):
    """
    Exercício resolvido 01
    Elaborar uma função conta_pares(min, max) para exibir todos os
    valores entre min e max, inclusive, com um incremento de 2,
    separando-os com um hífen. Ex.: 2 - 4 - 6 - 8 - 10 - 12 - 14.
    """
    if min % 2:
        min += 1
    for num in range(min, max + 1, 2):
        if num >= max - 1:
            print(num)
        else:
            print(num, end=" - ")

conta_pares(2, 8) # 2 - 4 - 6 - 8
conta_pares(1, 8) # 2 - 4 - 6 - 8
conta_pares(1, 9) # 2 - 4 - 6 - 8
conta_pares(2, 9) # 2 - 4 - 6 - 8

def fatorial(num):
    """
    Exercício resolvido 04
    Faça um programa que calcule o fatorial de um número inteiro
    positivo fornecido pelo usuário.
    Ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120.
    """
