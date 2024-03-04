"""
Programação Estruturada
2024.1
04/03/2024

Operadores
- Aritméticos
- Atribuição
- Comparação (ou relacionais)
- Lógicos (ou booleanos)
"""

# Operadores aritméticos
# Quando os operandos são numéricos:
x = 8.4
y = 7.2

print(x + y)  # soma
print(x - y)  # subtração
print(x * y)  # multiplicação
print(x / y)  # divisão
print(x ** y) # potência
print(x // y) # divisão inteira
print(x % y)  # módulo

print(round(x + y, 2))

# Quando pelo menos um operando é str:
print("Olá," + " mundo") # Concatenação de strings - str + str
print("-" * 30)          # Multiplicação de string - str * int

# Operadores de atribuição
x = 10
x += 2 # x = x + 2
x -= 1 # x = x - 1
x *= 2

# Não é muito comum usar
x /= 3 # x = x / 3
x **= 2
x //= 4
x %= 7
print(x)

# Operadores de comparação ou relacionais
# Retornam um booleano (True / False)
x = 10
y = 3

print("-" * 30)
print(x > y)  # maior que
print(x >= y) # maior ou igual a
print(x < y)  # menor que
print(x <= y) # menor ou igual a
print(x == y) # igual a
print(x != y) # diferente de

# Comparação entre strings
# https://pt.wikipedia.org/wiki/ASCII

x = "abc"
y = "aBc"

print("-" * 30)
print(x > y)  # maior que
print(x >= y) # maior ou igual a
print(x < y)  # menor que
print(x <= y) # menor ou igual a
print(x == y) # igual a
print(x != y) # diferente de

# Operadores lógicos
print("-" * 30)
print(True and False) # E
print(True or False)  # OU
print(not True)       # NÃO

print("-" * 30)
print(int(6.0))
print(float("10.42"))
print(bool("10"))

# Qualquer coisa diferente de 0, 0.0, "", [], (), {}, como True
"""
Operação and
- Se o primeiro operando é True, retorna o segundo operando
- Se o primeiro operando é False, retorna o primeiro operando

Operação or
- Se o primeiro operando é True, retorna o primeiro operando
- Se o primeiro operando é False, retorna o segundo operando
"""

print("a" and 16)  # 16
print(0 and "abc") # 0

# Se o 1º operando fosse True, subiria um erro
print("" and int("b")) # ""

print("a" or 16)    # "a"
print(0.0 or "abc") # "abc"

print(0.0 or "")       # ""
print(1.5 and "texto") # "texto"

# Pythonico
# nome = input("Informe o nome: ") or "Valor inválido"
# print(nome)

"""
Precedência

()
**
* / // %
+ -
> >= < <= == !=
not x
and
or

=
"""

print(4 + 6 / 2 ** 2 > 10 // 3 and 4.5 - 2 or not 10 % 3 <= 2)
print(4 + 6 / 4 > 10 // 3 and 4.5 - 2 or not 10 % 3 <= 2)
print(4 + 1.5 > 3 and 4.5 - 2 or not 1 <= 2)
print(5.5 > 3 and 2.5 or not 1 <= 2)
print(True and 2.5 or not True)
print(True and 2.5 or False)
print(2.5 or False)
print(2.5)

print((4 + 6 / 2) ** 2 > 10 // (3 and 4.5) - 2 or not 10 % 3 <= 2)
print((4 + 3.0) ** 2 > 10 // (3 and 4.5) - 2 or not 10 % 3 <= 2)
print(7.0 ** 2 > 10 // 4.5 - 2 or not 10 % 3 <= 2)
print(49.0 > 10 // 4.5 - 2 or not 10 % 3 <= 2)
print(49.0 > 2.0 - 2 or not 1 <= 2)
print(49.0 > 0.0 or not 1 <= 2)
print(True or not True)
print(True or False)
print(True)

"""
Nota de aula 04
Exercício resolvido 01
Faça um programa que peça as três notas da disciplina (AP1, AP2 e AC) e mostre
a média. A média é calculada de acordo com a fórmula
M = (AP1 + AP2) * 0.4 + AC * 0.2.
"""
ap1 = float(input("Informe a nota da AP1: "))
ap2 = float(input("Informe a nota da AP2: "))
ac = float(input("Informe a nota da AC: "))
media = (ap1 + ap2) * 0.4 + ac * 0.2
print("A média é", round(media, 2))
