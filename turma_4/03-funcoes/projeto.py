"""
Programação Estruturada
2024.1
01/03/2024

Aplicação de funções
"""

def soma(a, b):
    """*Recebe* dois valores e retorna a soma deles."""
    return a + b

def outra_soma():
    """*Lê* dois valores e retorna a soma deles."""
    a = float(input("Informe um número: "))
    b = float(input("Informe outro número: "))
    return a + b

def subtracao(a, b):
    return a - b

def main():
    print(soma(5, 8))
    print(soma(1, 9))
    print(outra_soma())
    print(subtracao(5, 8))

main()
