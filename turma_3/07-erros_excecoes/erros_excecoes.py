"""
Programação Estruturada
2024.1
16/04/2024

Tratamento de Erros e Exceções
- try / except / else / finally
"""

def divisao(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("não é possível dividir por zero.")
    # except TypeError:
    #     print("os tipos dos dados são inválidos.")
    except Exception as erro:
        print(f"erro do tipo {type(erro).__name__}: {erro}")

divisao(2, 5)
divisao(10, 2)
divisao(10, 0)
divisao('a', 2)

def terceira_letra():
    nome = input()
    try:
        print(f"Terceira letra: {nome[2]}")
    except IndexError:
        print("Nome curto demais.")
    else:
        print("Nome com três letras ou mais.")
    finally:
        print("Fim da função.")

# terceira_letra()

texto_lido = input()
if texto_lido.isnumeric():
    print("é numérico")
    numero = int(texto_lido)
