"""
Docstrings

Comentário de várias
linhas.

Programação Estruturada
26/02/2024

Introdução a Python
- Comentários
- Exibição de dados na tela
- Tipos de dados
- Leitura de dados
- Variáveis
- Alteração de tipos
"""

# Esta é uma linha de comentário.
# O interpretador ignora tudo que está à direita da #.

# Essa solução foi baseada na solução proposta por fulano.
# https://...

print("olá, mundo")    # olá, mundo
print("olá,", "mundo", end="\n\n") # olá,mundo
print("Ana tem", 18, "anos.", sep="--")

"""
Tipos de dados em Python

- 4 tipos de dados primitivos
    - Números inteiros (int)
    - Números decimais (float)
    - Booleanos (bool)
    - Texto (str)
"""

print(-10, 4, 8, 16, 358) # int
print(4.5, 8.2, -14.9)    # float
print(4,5) # 4 5
print(4.5) # 4.5
print(True, False)        # bool - 1bit

# Essas quatro linhas representam coisas diferentes!
print(2)
print(2.0)
print("2")
print("2.0")

# string
print("olá, mundo")
print('olá, mundo')
print("""representação
de um texto de múltiplas linhas""")
print('olá, "mundo"')
print("olá, 'mundo'")

# escape char - \
print("olá, \"mundo\"")
print("texto\nde duas linhas")
print("texto \\novo")
print("texto\tdeslocado")

# None
print(print("olá, mundo"))

# O resultado do input é SEMPRE uma string
# print(input("Informe o seu nome: "))
# print(type(input("Informe a sua idade: ")))

# nome = input("Informe o seu nome: ")
# print("Olá,", nome)

nome = "André"
print("Olá,", nome)

# Python é uma linguagem de tipagem fraca e dinâmica
nome = 48
print(nome)

# type hint
idade : int = 16
print(idade)

# Python não possui o conceito de constante
PI = 3.1415
TAM_MAXIMO = 15

print(type("2"))
print(type(int("2")))
print(type(2))

# idade = int(input("Informe sua idade: "))

print(str(4.5))
print(float("10.5"))
print(float(8))

# Todo dado diferente de 0, 0.0, "", etc. são considerados como True
print(bool(""))
print(bool("olá, mundo"))
print(bool(0))
print(bool(36.95))

x = 10

if x:
    print("Diferente de zero")
