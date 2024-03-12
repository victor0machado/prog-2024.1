"""
Programação Estruturada
2024.1
12/03/2024

Estruturas de repetição
Exercícios
"""

def conta_pares(min, max):
    """
    Exercício resolvido 01
    Elaborar uma função conta_pares(min, max) para exibir todos os valores pares
    entre min e max, com um incremento de 2, separando-os com um hífen.
    Ex.: conta_pares(2, 14) -> 2 - 4 - 6 - 8 - 10 - 12 - 14
    """
    if min % 2:
        min += 1
    for num in range(min, max + 1, 2):
        if num >= max - 1:
            print(num)
        else:
            print(num, end=" - ")

conta_pares(2, 10) # 2 - 4 - 6 - 8 - 10
conta_pares(1, 10) # 2 - 4 - 6 - 8 - 10
conta_pares(1, 11) # 2 - 4 - 6 - 8 - 10
conta_pares(2, 11) # 2 - 4 - 6 - 8 - 10
print("-" * 30)

def conta_pares2(min, max):
    """
    Exercício resolvido 01
    Elaborar uma função conta_pares(min, max) para exibir todos os valores pares
    entre min e max, com um incremento de 2, separando-os com um hífen.
    Ex.: conta_pares(2, 14) -> 2 - 4 - 6 - 8 - 10 - 12 - 14
    """
    if min % 2:
        min += 1
    texto = ""
    for num in range(min, max + 1, 2):
        texto += str(num)
        if num < max - 1:
            texto += " - "

    print(texto)

conta_pares2(2, 10) # 2 - 4 - 6 - 8 - 10
conta_pares2(1, 10) # 2 - 4 - 6 - 8 - 10
conta_pares2(1, 11) # 2 - 4 - 6 - 8 - 10
conta_pares2(2, 11) # 2 - 4 - 6 - 8 - 10
