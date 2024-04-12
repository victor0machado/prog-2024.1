"""
Programação Estruturada
2024.1
12/04/2024

Tratamento de erros e exceções
try / except / else / finally
- Uso quando não souber qual exceção pode subir
- OU quando sei qual exceção pode subir, mas não sei como o código chega lá
"""

def divisao(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Erro! O divisor não pode ser 0.")
    except TypeError:
        print("Erro! Ambos os parâmetros precisam ser numéricos.")
    except Exception as err:
        print(err)

def terceira_letra():
    nome = input("Informe seu nome: ")
    try:
        print(f"A terceira letra do seu nome é {nome[2]}.")
        ret = nome[2]
    except Exception as err:
        print(f"Erro desconhecido. Erro: {err}")
        print(type(err))
        ret = "erro!"
    else:
        print("Leitura dos dados bem-sucedida.")
    finally:
        print("fim da função")
        return ret

# divisao(10, 0)
# print(terceira_letra())

class TamanhoExcedidoError(Exception):
    pass

def exibe_num(numero):
    if numero > 10:
        raise TamanhoExcedidoError

    print(numero)

# exibe_num(15)

def func1():
    raise NotImplementedError

def func2():
    raise NotImplementedError

func1()
