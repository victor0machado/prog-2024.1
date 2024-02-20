"""
Este é um comentário de bloco.

Você pode ocupar múltiplas linhas.

Blocos de comentário no início do módulo são
chamados de _docstring_.
"""

# Essa é uma linha de comentário
print("olá, mundo") # linha de comentário

print("olá", ", mundo", sep="")

"""
Tipos de dados
- Primitivos:
    - Inteiros (int) -> -20, 12, 4, 19, 0
    - Decimais (float) -> 4.85, -10.5, 1.28
    - Lógicos ou booleanos (bool) -> True, False
    - Texto (string)

'olá, mundo'
"olá, mundo"

caractere de escape (escape char)
\" \'

"olá, \"mundo\""
'olá, "mundo"'

2   int
2.0 float
"2" string

0 "" [] () -> False

"""

print("olá, \"mundo\"")
print('olá, "mundo"\n')
print("contrabarra -> \\")
print("duas contrabarras -> \\\\")
print("olá,\nmundo")

print("----------------")
# A função print() retorna None
print(print("olá, mundo")) # Vai imprimir None

print("Maria tem", 20, "anos.")

# print(input("Informe o seu nome: "))
# print(type(input("Informe a sua idade: ")))
print(type(4.5))

nome = input("Informe o seu nome: ")

print(nome)
nome = "abcd"
print(nome)

# constante
PI = 3.1415

# Python é uma linguagem de tipagem fraca e dinâmica
nome = 14 # isso é possível, mas não recomendado

idade = int(input("Informe a sua idade: "))
print(type(idade))
print(bool("texto"))
