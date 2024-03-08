"""
Programação Estruturada
2024.1
08/03/2024

Estruturas de Decisão - Nota de aula 06
Exercícios
"""

"""
Exercício resolvido 02
Implemente um programa que receba dois números e retorne o maior deles.
"""
def maior(n1, n2):
    if n1 > n2:
        return n1
    return n2

# Solução com ternário
def maior2(n1, n2):
    return n1 if n1 > n2 else n2

"""
Exercício resolvido 04
Faça um programa que verifique se uma letra é vogal ou consoante.
"""
def e_vogal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return "é vogal"
    return "é consoante"

print(e_vogal("j"))
print(e_vogal("a"))

def e_vogal2(letra):
    match letra:
        case "a" | "e" | "i" | "o" | "u":
            return "é vogal"
    return "é consoante"

print(e_vogal2("j"))
print(e_vogal2("a"))

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

def aprovacao(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if nota_e_valida(n1) and nota_e_valida(n2) and nota_e_valida(n3):
        if 7 <= media < 10:
            print("Aprovado")
        elif 0 <= media < 7:
            print("Reprovado")
        elif media == 10:
            print("Aprovado com distinção")
    else:
        print("Nota inválida")

aprovacao(10, 10, 10) # Aprovado com dinstição
aprovacao(10, 8, 9)   # Aprovado
aprovacao(6, 5, 5)    # Reprovado
aprovacao(11, 9, 10)  # Nota inválida
aprovacao(11, 11, 11) # Nota inválida
aprovacao(-1, -1, -1) # Nota inválida
