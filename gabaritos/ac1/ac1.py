"""
Programação Estruturada
2024.1

AC1
Gabarito
"""

# Exercício 1
a = float(input("Informe o parâmetro a da equação: "))
b = float(input("Informe o parâmetro b da equação: "))
c = float(input("Informe o parâmetro c da equação: "))

delta = b ** 2 - 4 * a * c
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)

print("A primeira raiz da equação é", x1)
print("A segunda raiz da equação é", x2)

# Exercício 2
ano = int(input("Informe o ano: "))
print(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0)
