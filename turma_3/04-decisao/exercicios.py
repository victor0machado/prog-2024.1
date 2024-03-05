"""
Programação Estruturada
2024.1
05/03/2024

Exercícios - Nota de aula 06
"""

"""
Exercício resolvido 02
Implemente um programa que receba dois números e retorne o maior deles.
"""
def maior(n1, n2):
    if n1 > n2:
        return n1

    return n2

def maior2(n1, n2):
    return n1 if n1 > n2 else n2

def le_dois_numeros():
    n1 = int(input("Informe um número: "))
    n2 = int(input("Informe outro número: "))
    return n1, n2

"""
Exercício 04
Faça um programa que verifique se uma letra é vogal ou consoante.
"""
def e_vogal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return True

    return False

def e_vogal(letra):
    match letra:
        case "a" | "e" | "i" | "o" | "u":
            return True
    return False

def main():
    # x, y = le_dois_numeros()
    # print(maior2(x, y))
    print(maior(1, 3))
    print(maior2(6, 4))
    print(e_vogal("j"))

main()
