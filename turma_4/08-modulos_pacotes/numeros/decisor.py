"""
Seleciona qual operação será realizada conforme o input do usuário.
"""
from numeros.operacoes import arit
# usamos ref relativas quando lido com módulos dentro de um mesmo pacote
from .operacoes import exp # usando uma referência relativa

def chama_calculadora(n1, n2, operacao):
    match operacao:
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
        case "^":
            return exp.raiz(n1, n2)
        case _:
            return "erro! operação inválida"

