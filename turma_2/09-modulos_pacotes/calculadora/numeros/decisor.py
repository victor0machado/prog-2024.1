"""
Define qual será a operação realizada.
"""
# Referência relativa
from .operacoes import arit
from .operacoes import exp

def selecionar_operacao(n1, n2, oper):
    match oper:
        case "+":
            print(arit.soma(n1, n2))
        case "-":
            print(arit.subtracao(n1, n2))
        case "*":
            print(arit.multiplicacao(n1, n2))
        case "/":
            print(arit.divisao(n1, n2))
        case "**":
            print(exp.potencia(n1, n2))
        case "^":
            print(exp.raiz(n1, n2))
