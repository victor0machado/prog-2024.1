"""
Interface por linha de comando para a calculadora simples.
"""
from ..numeros import decisor

def iniciar():
    n1 = float(input("Informe um número: "))
    oper = input("Informe a operação (+, -, *, /, **, ^): ")
    n2 = float(input("Informe outro número: "))

    decisor.selecionar_operacao(n1, n2, oper)
