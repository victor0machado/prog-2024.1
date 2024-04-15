"""
Programação Estruturada
2024.1
15/04/2024

Tratamento de Erros e Exceções
- try / except / else / finally
"""

def divisao(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Erro! Divisão por zero")
    # except TypeError:
    #     print("Erro! Os tipos são incompatíveis")
    except Exception as erro:
        print(f"Erro do tipo {type(erro).__name__}: {erro}")

divisao(10, 2)
divisao(3, 5)
divisao(3, 0)   # ZeroDivisionError
divisao('a', 2) # TypeError

def terceira_letra():
    nome = input()
    try:
        print(f"A terceira letra é {nome[2]}.")
    except IndexError:
        print("O nome precisa ter pelo menos três letras.")
    else: # só entra se não surgiu uma exceção
        print("Leitura feita com sucesso.")
    finally: # entra sempre
        print("Fim do try.")

# terceira_letra()

def divisao2(a, b):
    if b == 0:
        raise ValueError

# divisao2(2, 0)

def func1():
    raise NotImplementedError

def func2():
    raise NotImplementedError

def func3():
    raise NotImplementedError

class TamanhoExcedidoError(Exception):
    pass

lista = [1, 2, 3, 4, 5]

if len(lista) > 8:
    raise TamanhoExcedidoError
