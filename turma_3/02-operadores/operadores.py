"""
Programação Estruturada
2024.1
27/02/2024

Operadores em Python
- Aritméticos
- Atribuição
- Comparação
- Operadores lógicos
"""

# Operadores aritméticos
# Utilizando números apenas (int ou float)
x = 8.4
y = 2.7

print(x + y) # soma
print(x - y) # subtração
print(x * y) # multiplicação
print(x / y) # divisão
print(x ** y) # potência
print(x // y) # divisão inteira
print(x % y)  # módulo

print(round(x % y, 1))  # módulo

# Utilizando strings
z = "-"
print(z + z) # posso utilizar str com str para adição
print(30 * z) # posso utilizar int com str para multiplicação

# Operadores de atribuição
x = 10
x += 1 # x = x + 1
x -= 1 # x = x - 1
x *= 2 # x = x [oper] [num]
x /= 3
x **= 2
x //= 4
x %= 2
print(x)

# Operadores de comparação
# Retornam um dado bool, True ou False

print(x > y)  # maior que
print(x < y)  # menor que
print(x >= y) # maior ou igual a
print(x <= y) # menor ou igual a
print(x == y) # igual a
print(x != y) # diferente de

z = "abc"
w = "Abc"
print("-" * 20)

# A comparação é feita conforme a tabela ASCII
# https://pt.wikipedia.org/wiki/ASCII
print(z > w)
print(z < w)
print(z >= w)
print(z <= w)
print(z == w)
print(z != w)

# Operadores lógicos
x = True
y = False

print(x and y) # E
print(x or y)  # OU
print(not x)   # NÃO

# Precedência de operadores
"""
()
**
* / // %
+ -
< <= > >= == !=
not
and
or
"""

x = 10
y = 3
print(x > 4 and y * 3 <= x) # True
print(10 / 2 * 5) # 25
print(not (x + 4 * y - 2 < 10) and 10 ** y % 2 == 1) # False
print(not (x + 4 * (y - 2) < 10) and 10 ** y % 2 == 1) # False

# Em Python, tudo que não é 0, 0.0, "", [], {}, etc. é True
print(not (x + 4 * (y - 2)) and 10 ** y % 2 == 1)

print("-" * 30)
# Operações com or
# Se o primeiro operando é verdadeiro, retorna o primeiro operando
print("10" or False)
print(7.5 or 2)

# Se o primeiro operando é falso, retorna o segundo operando
print("" or 16)
print(0 or "")
print(False or "10")

# Operações com and
# Se o primeiro operando é falso, retorna o primeiro operando
print("" and 15)
print(0 and False)

# Se o primeiro operando é verdadeiro, retorna o segundo operando
print(1.2 and 0.0)
print("abc" and False)

# Pythonico
# nome = input("Informe o seu nome: ") or "Valor inválido"
# print(nome)

print("-" * 30)
print("ex 1")

ap1 = float(input("Informe a nota da AP1: "))
ap2 = float(input("Informe a nota da AP2: "))
ac = float(input("Informe a nota da AC: "))

print("A nota final é", round((ap1 + ap2) * 0.4 + ac * 0.2, 2))
