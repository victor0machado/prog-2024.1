"""
Programação Estuturada
2024.1
28/02/2024

Operadores
- Aritméticos
- Atribuição
- Comparação (ou relacionais)
- Lógicos (ou booleanos)
"""

# Operadores aritméticos
# Quando ambos os operandos são números:

x = 7.4
y = 5.2

print(x + y)  # soma
print(x - y)  # subtração
print(x * y)  # multiplicação
print(x / y)  # divisão
print(x // y) # divisão inteira
print(x % y)  # módulo
print(x ** y) # potência

print(round(x + y, 1))

# Quando um dos operandos for uma str:

print("-" * 30)
print("-" + "+")

# Operadores de atribuição

x = 2
x += 1  # x = x + 1
x -= 4  # x = x - 4

# A partir daqui, é bem incomum de usar
x *= 6  # x = x * 6
x /= 2
x //= 4
x **= 2
x %= 5
print(x)

# Operadores de comparação
# Sempre vão retornar um booleano (True / False)

print("-" * 30)
print(x > y)  # maior que
print(x < y)  # menor que
print(x >= y) # maior ou igual a
print(x <= y) # menor ou igual a
print(x == y) # igual a
print(x != y) # diferente de

# Comparação de strings é feita através dos códigos ASCII
# https://pt.wikipedia.org/wiki/ASCII
z = "ab"
w = "Abc"

print("-" * 30)
print(z > w)  # maior que
print(z < w)  # menor que
print(z >= w) # maior ou igual a
print(z <= w) # menor ou igual a
print(z == w) # igual a
print(z != w) # diferente de

# Operadores lógicos

a = True
b = False

print(a and b) # E
print(a or b)  # OU
print(not a)   # NÃO

print("-" * 30)
# Type casting
# idade = int(input("Informe sua idade: "))
# print("Sua idade é " + str(idade))
print(bool(""))
print(bool(0))
print(bool(0.0))
print(bool("10"))
print(bool(12.5))
print(bool(1))

print("10" or 75)
print(True or 0)
print(False or "abc")
print("" or 10.5)

texto = "abc"
print(0 and int(texto))
print(10 and "")
print(10 and "abc")

# Pythonico
# nome = input("Informe o seu nome: ") or "Valor inválido"

# print(nome)

"""
Precedência de operadores

()
**
* / // %
+ -
< <= > >= == !=
not
and
or
"""

print("-" * 30)
print(4 > 2 * 3 ** 2 - 7 and 4 * 6 - 7 // 2 or not 10 + 2 <= 5)
"""
4 > 2 * 9 - 7 and 4 * 6 - 7 // 2 or not 10 + 2 <= 5
4 > 18 - 7 and 24 - 3 or not 10 + 2 <= 5
4 > 11 and 21 or not 12 <= 5
False and 21 or not False
False and 21 or True
False or True
True
"""

print(4 > 2 * 3 ** 2 - (7 and 4) * (6 - 7) // 2 or (not 10 + 2) <= 5)
"""
4 > 2 * 3 ** 2 - 4 * -1 // 2 or (not 12) <= 5
4 > 2 * 3 ** 2 - 4 * -1 // 2 or False <= 5
4 > 2 * 9 - 4 * -1 // 2 or False <= 5
4 > 18 + 4 // 2 or False <= 5
4 > 18 + 2 or False <= 5
4 > 20 or False <= 5
False or True
True
"""

print("-" * 30)
"""
Exercício
Faça um programa que peça as três notas da disciplina (AP1, AP2 e AC) e mostre
a média. A média é calculada de acordo com a fórmula
M = (AP1 + AP2) * 0.4 + AC * 0.2.
"""
ap1 = float(input("Informe a nota da AP1: "))
ap2 = float(input("Informe a nota da AP2: "))
ac = float(input("Informe a nota da AC: "))

print("A média é", round((ap1 + ap2) * 0.4 + ac * 0.2, 2))
