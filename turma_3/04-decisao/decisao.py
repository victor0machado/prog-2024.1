"""
Programação Estruturada
2024.1
05/03/2024

Estruturas de Decisão
- if/elif/else

if <teste>:
    <codigo>

- match/case
"""

def robo_educado(turno):
    if turno == "M":
        print("Bom dia!")
    elif turno == "T": # else if
        print("Boa tarde!")
    elif turno == "N":
        print("Boa noite!")
    else:
        print("Horário inválido!")

def robo_educado2(turno):
    if turno == "M":
        return "Bom dia!"

    if turno == "T":
        return "Boa tarde!"

    # ...

def le_nome():
    nome = input("Informe o seu nome: ")
    # Solução mais "elegante"
    if not nome:
        print("Nenhum nome foi lido.")

    if nome == "":
        print("Nenhum nome foi lido.")

def saudacao(turno):
    # Usamos o match/case quando queremos comparar
    # uma variável a diferentes valores
    match turno:
        case "M":
            print("Bom dia!")
        case "T":
            print("Boa tarde!")
        case "N":
            print("Boa noite!")
        # O case _ é opcional
        case _: # equivalente ao else, não entrou em nenhuma outra opção
            print("Horário inválido!")

def aprovacao(conceito):
    if conceito == "Bom" or conceito == "Ótimo" or conceito == "Excelente":
        print("Aprovado")
    else:
        print("Reprovado")

    match conceito:
        case "Bom" | "Ótimo" | "Excelente":
            print("Aprovado")
        case _:
            print("Reprovado")

def e_par(num):
    if num % 2 == 0:
        return "é par"
    else:
        return "é ímpar"

def e_par2(num):
    if num % 2 == 0:
        return "é par"
    return "é ímpar"

# Solução pythonica para e_par()
# Ternário
def e_par3(num):
    return "é par" if not num % 2 else "é ímpar"

# Evitar usar ternário nessa situação
def robo_educado3(turno):
    return "Bom dia!" if turno == "M" else "Boa tarde!" if turno == "T" else "Boa noite!" if turno == "N" else "Horário inválido!"

def soma(a, b):
    return a + b

def main():
    robo_educado("M")
    robo_educado("T")
    robo_educado("abc")
    # le_nome()
    e_par2(11)
    x = soma(2, 5)
    print(x)

main()
