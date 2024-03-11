"""
Programação Estruturada
2024.1
11/03/2024

Estruturas de Decisão
Nota de aula 06
"""

"""
Exercício resolvido 02
Implemente um programa que receba dois números e retorne o maior deles.
"""
def maior(a, b):
    return a if a > b else b

print(maior(10, 5)) # 10
print(maior(5, 10)) # 10

"""
Exercício resolvido 04
Faça um programa que verifique se uma letra é vogal ou consoante.
"""
def e_vogal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return "vogal"
    return "consoante"

def e_vogal2(letra):
    match letra:
        case "a" | "e" | "i" | "o" | "u":
            return "vogal"
    return "consoante"

print(e_vogal2("j"))
print(e_vogal2("e"))

"""
Exercício resolvido 05
Faça um programa que receba três notas, calcule sua média aritmética simples e
apresente na tela uma das seguintes informações:

- A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
- A mensagem “Reprovado”, se a média for menor do que sete;
- A mensagem “Aprovado com Distinção”, se a média for igual a dez;
- A mensagem “Nota inválida!” toda vez que for inserido um valor inválido.
"""
def nota_e_valida(nota):
    return 0 <= nota <= 10

def calcula_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if nota_e_valida(nota1) and nota_e_valida(nota2) and nota_e_valida(nota3):
        if media == 10:
            print("Aprovado com distinção")
        elif 7 <= media < 10:
            print("Aprovado")
        else:
            print("Reprovado")
    else:
        print("Nota inválida!")

calcula_media(10, 10, 10) # Aprovado com distinção
calcula_media(7, 10, 10)  # Aprovado
calcula_media(3, 3, 3)    # Reprovado
calcula_media(15, 12, 7)  # Nota inválida
calcula_media(-5, -2, 0)  # Nota inválida
calcula_media(11, 10, 9)  # Nota inválida

