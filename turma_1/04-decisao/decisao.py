"""
Programação Estruturada
2024.1
11/03/2024

Estruturas de decisão
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
        print("Dado inválido!")

saudacao("M")
saudacao("T")
saudacao("N")
saudacao("abc")
print("-" * 30)

def saudacao2(turno):
    if turno == "M":
        return "Bom dia!"
    if turno == "T":
        return "Boa tarde!"
    if turno == "N":
        return "Boa noite!"
    return "Dado inválido!"

print(saudacao2("M"))
print(saudacao2("T"))
print(saudacao2("N"))
print(saudacao2("abc"))
print("-" * 30)

def le_nome():
    nome = input("Informe seu nome: ")
    if not nome:
        print("Nome inválido!")

# Ternários
def e_par(num):
    if num % 2:
        return "é ímpar"
    return "é par"

def e_par(num):
    return "é ímpar" if num % 2 else "é par"

# match/case
def saudacao3(turno):
    match turno:
        case "M":
            print("Bom dia!")
        case "T":
            print("Boa tarde!")
        case "N":
            print("Boa noite!")
        case _: # wildcard, opcional
            print("Dado inválido!")

def aprovacao(conceito):
    match conceito:
        case "Bom" | "Ótimo" | "Excelente":
            print("Aprovado")
        case _:
            print("Reprovado")
