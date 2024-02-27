"""
Programação Estruturada
2024.1
27/02/2024

Funções - Aplicação
"""

def soma(a, b):
    return a + b

def testa_soma():
    print("Testando a função soma()")
    x = float(input("Informe um número: "))
    y = float(input("Informe outro número: "))
    print("O resultado da soma é", soma(x, y))

def subtracao(a, b):
    return a - b

def testa_subtracao():
    print("Testando a função subtracao()")
    x = float(input("Informe um número: "))
    y = float(input("Informe outro número: "))
    print("O resultado da subtração é", subtracao(x, y))

def main():
    testa_soma()
    testa_subtracao()

main()
