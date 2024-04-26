"""
Interface por linha de comando (CLI)
Calculadora

Apresenta as opções da calculadora, e as operações disponíveis.
Chama as operações de cálculo, conforme a seleção do usuário.
"""
# Referência absoluta - pacotes diferentes dentro de um mesmo projeto
from numeros import decisor

def exibe_mensagem():
    print("""Bem-vindo à calculadora!
Insira um número e pressione ENTER, em seguida digite uma operação (+, -, *, /, **, ^) e pressione ENTER.
Por fim, insira outro número e pressione ENTER mais uma vez. O resultado será exibido em seguida.""")

def iniciar():
    exibe_mensagem()
    n1 = float(input())
    operacao = input()
    n2 = float(input())
    print(n1, operacao, n2, "=", decisor.chama_calculadora(n1, n2, operacao))
