"""
Define qual operação matemática será executada.
"""
# Referência relativa
from .operacoes import arit, exp

def executar(n1, n2, oper):
    """
    Executa a função matemática conforme a operação fornecida.

    Retorna um valor numérico que representa o resultado da função matemática.
    """
    match oper:
        case "+":
            return arit.soma(n1, n2)
        case "-":
            return arit.subtracao(n1, n2)
        case "*":
            return arit.multiplicacao(n1, n2)
        case "/":
            return arit.divisao(n1, n2)
        case "**":
            return exp.potencia(n1, n2)
        case "v":
            return exp.raiz(n1, n2)
