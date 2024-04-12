"""
Programação Estruturada
2024.1
12/04/2024

Tratamento de erros e exceções
try / except
"""

def divisao(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Erro! Divisão por zero.")
    except Exception as erro:
        print(f"Erro desconhecido do tipo {type(erro).__name__}: {erro}")

divisao(10, 2)
divisao(2, 5)
divisao(2, 0)
divisao('a', 2)

def terceira_letra():
    nome = input()
    try:
        print(f"A terceira letra é {nome[2]}")
    except Exception as erro:
        print(f"Erro: {erro}")
    else:
        print("fim da função")
    finally:
        print("fim da função de verdade.")

terceira_letra()
