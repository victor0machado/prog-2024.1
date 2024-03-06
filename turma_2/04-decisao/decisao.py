"""
Programação Estruturada
2024.1
06/03/2024

Estruturas de decisão (ou seleção)
- if/elif/else
- match/case
"""

def saudacao(turno):
    if turno == "M":
        print("Bom dia!")
    elif turno == "T":
        print("Boa tarde!")
    elif turno == "N":
        print("Boa noite!")
    else:
        print("Informação inválida!")

saudacao("T")
saudacao("N")
saudacao("M")
saudacao("A")

def saudacao2(turno):
    if turno == "M":
        return "Bom dia!"
    if turno == "T":
        return "Boa tarde!"
    if turno == "N":
        return "Boa noite!"

    return "Informação inválida!"

# Ternários
def e_par(num):
    return "é par" if num % 2 == 0 else "é ímpar"
    # if num % 2 == 0:
    #     return "é par"
    # return "é ímpar"

def e_par2(num):
    return num % 2 == 0

def le_nome():
    nome = input("Informe o seu nome: ")
    if nome == "":
        print("Nome inválido!")

    # Usar dessa forma é mais comum
    if not nome:
        print("Nome inválido!")

    return nome

def avaliacao(conceito):
    if conceito == "Bom" or conceito == "Ótimo" or conceito == "Excelente":
        print("Aprovado")
    else:
        print("Reprovado")

def avaliacao2(conceito):
    match conceito:
        case "Bom":
            print("Aprovado")
        case "Ótimo":
            print("Aprovado")
        case "Excelente":
            print("Aprovado")
        case _: # default case, opcional
            print("Reprovado")

def avaliacao3(conceito):
    match conceito:
        case "Bom" | "Ótimo" | "Excelente":
            print("Aprovado")
        case _:
            print("Reprovado")
