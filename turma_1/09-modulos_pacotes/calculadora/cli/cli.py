"""
Interface de texto para o programa.
"""
from .opcoes import opcoes

def rodar():
    print("Bem-vindo ao programa!")
    a = int(input("Informe o primeiro valor: "))
    b = int(input("Informe o segundo valor: "))

    opcao = input("Informe a operação (+, -, *, /): ")
    operacao = opcoes.analisar(opcao)
    if operacao is not None:
        print(operacao(a, b))


