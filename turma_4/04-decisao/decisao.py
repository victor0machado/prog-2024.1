"""
Programação Estruturada
2024.1
08/03/2024

Estruturas de decisão
- if/elif/else
- match/case
"""

def saudacao(turno):
    if turno == "M":
        print("Bom dia!")
    # else:
    #     if turno == "T":
    #         codigo
    elif turno == "T":  # else if
        print("Boa tarde!")
    elif turno == "N":
        print("Boa noite!")
    else:
        print("Dado inválido!")

def saudacao2(turno):
    if turno == "M":
        return "Bom dia!"
    if turno == "T":
        return "Boa tarde!"
    if turno == "N":
        return "Boa noite!"
    return "Dado inválido!"

saudacao("N")
saudacao("M")
saudacao("T")
saudacao("A")

print("-" * 30)
saudacao2("M")
saudacao2("N")

def le_nome():
    nome = input("Informe o seu nome: ")
    # if nome == "":
    if not nome:
        print("Erro! Entrada inválida.")

    return nome

# Ternário
def e_par(num):
    if num % 2:
        return "é ímpar"
    return "é par"

def e_par2(num):
    return "é ímpar" if num % 2 else "é par"

def saudacao3(turno):
    match turno:
        case "M":
            print("Bom dia!")
        case "T":
            print("Boa tarde!")
        case "N":
            print("Boa noite!")
        case _: # default case, opcional
            print("Dado inválido!")

# _ -> wildcard variable

saudacao3("M")
saudacao3("T")
saudacao3("N")
saudacao3("A")

def aprovacao(conceito):
    match conceito:
        case "Bom" | "Ótimo" | "Excelente":
            return "Aprovado"
        case _:
            return "Reprovado"
