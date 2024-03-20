"""
Programação Estruturada
2024.1
20/03/2024

Estruturas de Dados
Listas
- Mutáveis
- Ordenados

Tuplas
- Imutáveis
- Ordenados
"""

lista = ["abc", 12, 4.5, True, print("olá")]

letras = ["a", "b", "c", "d", "e", "f", "g"]
print(letras[3]) # d
letras[5] = "h"
print(letras)
# print(letras[10]) -> IndexError
print(letras[-1])

print(list(range(5)))

# Slicing, ou fatiamento, de listas
print(letras[1:3])
print(letras[1:])   # do índice 1 até o fim
print(letras[:3])
print(letras[:])    # do início ao fim
print(letras[::2])  # do início ao fim, de 2 em 2
print(letras[::-1]) # inverte a lista

texto = "olá, mundo"
print(texto[::-1])

# matriz
coordenadas = [[1, 0], [5, 3], [-2, 4]]
print(coordenadas[1][1])

print("-" * 30)

matriz = [
    [1, 3, 4, 5],
    [7, 0, 1, 2],
    [3, 9, 8, 0],
    [1, 2, 3, 4]
]

# operador in / not in
print("f" in letras)
print("k" not in letras)

if "h" in letras:
    print("A letra h está na lista.")

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()

for indice, letra in enumerate(letras):
    print(indice, letra, sep=" - ")

alunos = ["antonio", "ana", "josé"]
notas = [6.5, 7.7, 4.3]

for aluno, nota in zip(alunos, notas):
    print("A nota do aluno", aluno, "foi", nota)

print("-" * 30)
print(len(alunos))
alunos.append("maria")
print(alunos)
nome_excluido = alunos.pop()
print(alunos)
print(nome_excluido)

alunos_ordenados = sorted(alunos) # Ordena a lista sem in-place
print(alunos_ordenados)
print(alunos)

print("-" * 30)
alunos.sort(reverse=True) # Ordena a lista in-place
print(alunos)

# Passagem por valor vs passagem por referência
print("-" * 30)
x = 2
y = x
print(x, y)

x = 3
print(x, y)

x = []
y = x
print(x, y)

x.append(2)
print(x, y)

def inclui_valor(a, valor):
    a.append(valor)

b = []
inclui_valor(b, 1)
print(b)

def inclui_valor2(a, valor):
    b = a.copy()
    b.append(valor)
    return b

print("-" * 30)
b = []
c = inclui_valor2(b, 2)
print(b, c)

def aumenta_lista2(lista=None):
    if lista is None:
        lista = []
    lista.append(10)
    return lista

print("-" * 30)
x = aumenta_lista2()
print(x)
y = aumenta_lista2()
print(y)

print("-" * 30)
# Pythonico
# Compreensão de listas
a = [1, 2, 3, 4, 5, 6, 7]
b = []
for elem in a:
    b.append(elem ** 2)
print(b)

b = [elem ** 2 for elem in a]
print(b)

b = [elem ** 2 for elem in a if elem % 2 == 1]
print(b)

print("-" * 30)
print(matriz)
b = [elem for linha in matriz for elem in linha]
print(b)

"Olá, mundo".split(", ") # ["Olá", "mundo"]

numeros = [1, 3, 5, 7]
texto = ", ".join([str(num) for num in numeros])
print(f"As cartas são {texto}")

palavra = "olá"
for letra in palavra:
    print(letra)

# Tupla
tupla = (1, 2, 3)
print(tupla)
print(tupla[2])

# tupla[1] = 7 -> TypeError
print(list(tupla))

def le_notas():
    n1 = input()
    n2 = input()
    return n1, n2

notas = list(le_notas())
print(notas)
