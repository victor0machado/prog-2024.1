"""
Programação Estruturada
2024.1
01/03/2024

Operações em Python
- Aritméticas
- Atribuição
- Comparação (ou Relacionais)
- Lógicas (ou Booleanas)
"""

# Operações Aritméticas
# Dois operandos numéricos
x = 8.4
y = 2.3

print(x + y)  # Soma
print(x - y)  # Subtração
print(x * y)  # Multiplicação
print(x / y)  # Divisão
print(x ** y) # Potência
print(x // y) # Divisão inteira
print(x % y)  # Módulo

# round(valor, num_digitos)
print(round(x - y, 2))

# Um operando é uma str
print("-" + "-") # concatenação de strings
print("-" * 30)  # multiplicação de strings

# Operações de atribuição
x = 10

# Mais comuns
x += 2  # x = x + 2
x -= 3  # x = x - 3

# Menos comuns
x *= 5  # x = x * 5
x /= 4
x **= 2
x //= 6
x %= 2
print(x)
print(y)

# Operadores de comparação
# Resultam num valor booleano (True ou False)
print(x > y)  # maior que
print(x >= y) # maior ou igual a
print(x < y)  # menor que
print(x <= y) # menor ou igual a
print(x == y) # igual a
print(x != y) # diferente de

# Comparação entre strings - tabela ASCII
# https://pt.wikipedia.org/wiki/ASCII

print("-" * 30)
x = "Fbc"
y = "abc"
print(x > y)  # maior que
print(x >= y) # maior ou igual a
print(x < y)  # menor que
print(x <= y) # menor ou igual a
print(x == y) # igual a
print(x != y) # diferente de

# Operadores lógicos
print("-" * 30)

x = True
y = False
print(x and y) # E
print(x or y)  # OU
print(not x)   # NÃO

# type casting
x = 9
print(float(x))
print(int("10"))

# Em Python, tudo que for diferente de "", 0, 0.0, é True
print(bool(x))
print(bool(0))

print("abc" and 16)
print(0 and 16)
print(False and 16)
print("" and 16)

print("abc" or 16)
print(10.5 or 16)
print(True or 16)
print("" or 16)

# Isso sobe uma exceção se o primeiro operando for False
print(6 or int("a"))

# Pythonico
nome = input("Informe o seu nome: ") or "Valor inválido"

print(nome)

"""
Precedência

()
**
* / // %
+ -
> >= < <= == !=
not
and
or
"""

print(6 + 3 * 2 <= 15 - 2.5 // 4 % 3 and 10 / 2 or not 15 + 2 ** 2 < 2)
print(6 + 3 * 2 <= 15 - 2.5 // 4 % 3 and 10 / 2 or not 15 + 4 < 2)
print(6 + 6 <= 15 - 1.0 % 3 and 5.0 or not 15 + 4 < 2)
print(6 + 6 <= 15 + 2.0 and 5.0 or not 15 + 4 < 2)
print(12 <= 17.0 and 5.0 or not 19 < 2)
print(True and 5.0 or not False)
print(True and 5.0 or True)
print(5.0 or True)
print(5.0)

print(6 + 3 * 2 <= 15 - (2.5 // 4 % 3 and 10 / 2) or not 15 + 2 ** 2 < 2)
print(6 + 6 <= 15 - (0.0 % 3 and 5.0) or not 15 + 4 < 2)
print(12 <= 15 - (0.0 and 5.0) or not 19 < 2)
print(12 <= 15 - 0.0 or not 19 < 2)
print(12 <= 15 or not 19 < 2)
print(True or not False)
print(True or True)
print(True)
