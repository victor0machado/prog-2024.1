"""
Opções de cálculo no programa.
"""
from ...numeros import operacoes

def analisar(opcao):
    match opcao:
        case "+":
            return operacoes.soma
        case "-":
            return operacoes.subtracao
        case "*":
            return operacoes.multiplicacao
        case "/":
            return operacoes.divisao
        case _:
            return None
