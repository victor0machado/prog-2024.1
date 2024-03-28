"""
Programação Estruturada
2024.1

AC3
Gabarito
"""

def determina_tipo_triangulo(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        return "Não é um triângulo"
    if a == b and a == c:
        return "Equilátero"
    if a == b or a == c or b == c:
        return "Isósceles"
    return "Escaleno"

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

def dia_semana(dia):
    match dia:
        case 1:
            return "domingo"
        case 2:
            return "segunda-feira"
        case 3:
            return "terça-feira"
        case 4:
            return "quarta-feira"
        case 5:
            return "quinta-feira"
        case 6:
            return "sexta-feira"
        case 7:
            return "sábado"
        case _:
            return ""

def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def calculadora():
    n1 = float(input("Informe um número: "))
    n2 = float(input("Informe outro número: "))
    oper = input("Informe a operação: ")
    match oper:
        case "soma":
            print("Resultado:", soma(n1, n2))
        case "subtração":
            print("Resultado:", subtracao(n1, n2))
        case "multiplicação":
            print("Resultado:", multiplicacao(n1, n2))
        case "divisão":
            print("Resultado:", divisao(n1, n2))
        case _:
            print("operação inválida")

def main():
    testa_triangulo()
    testa_dia_semana()
    calculadora()

main()
