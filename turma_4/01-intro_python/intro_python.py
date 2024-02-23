"""
Este é um comentário de bloco.
O interpretador ignora todas as linhas.

Ele é muito utilizado em início de módulo e em explicações de funções.
Chamamos isso de _docstring_.
"""

# Este é um comentário de uma linha
# Você pode escrever vários comentários de uma linha
print("olá, mundo!", end=" -- ")
print("olá,", " mundo", "!", sep="", end="\n\n")
print("Maria tem", 25, "anos.", end=" -- ")

"""
4 Tipos primitivos de dados:
- Numéricos inteiros (int)
- Numéricos reais (float) --> floating point
- Texto (string)
- Booleanos (bool) --> True False
"""

print(14, -10, 25, 84) # int
print(14.1, -4.5, 16.42) # float
print(True, False) # bool

# string
print("olá, mundo")
print('olá, mundo')
print("""Esta é uma
string com várias
linhas""")

# Uso de escape char (\)
print("olá, \"mundo\"")
print('olá, "mundo"')
print("olá,\nmundo")
print("C:\\Projetos")

# Os dados abaixo são diferentes!
print(2)
print(2.0)
print("2")
print("2.0")

print("----------------")
print(print("olá, mundo!"))

# Entrada de dados - io
print(input("Informe o seu nome: "))

nome = input("Informe o seu nome: ")
print("Olá,", nome)

idade = 35
print("Você tem", idade, "anos.")

# Python é uma linguagem fracamente tipada e de tipagem dinâmica

x = idade
idade = "olá"
print(idade)
print(x)

matricula_aluno = "12334"
MAX_VALORES = 32

print(MAX_VALORES)
