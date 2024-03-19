"""
Programação Estruturada
2024.1
19/03/2024

Estruturas de Dados
Listas
- Mutáveis
- Ordenados

Tuplas
- Imutáveis
- Ordenados
"""

alunos = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# É possível ter dados diferentes dentro de uma mesma lista, porém não é
# recomendado
lista = [123, "abc", print("olá"), range, True]

print(alunos)
print(alunos[2])
print(alunos[-1]) # último
# print(alunos[15]) -> vai subir um IndexError, o índice não existe

# slicing
print(list(range(2, 20, 5))) # 2, 7, 12, 17
print(alunos[2:8:2])
print(alunos[:8:2]) # inicia no início da lista
print(alunos[2::2]) # termina no final da lista
print(alunos[2:8])
print(alunos[::2])
print(alunos[::-1]) # inverte a lista

# matriz
coordenadas = [[2, 6], [1, 8], [-10, 5]]
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(matriz[3])
print(matriz[3][2])

# Operador in / not in
print("g" in alunos) # True
print("z" in alunos) # False

for cont in range(10):
    print(cont)

print("-" * 30)
for aluno in alunos:
    print(aluno, end=" ")
print()

# nome = input("Informe o seu nome: ")
# if nome not in alunos:
#     print("Você não está na chamada!")

print("-" * 30)
for indice, aluno in enumerate(alunos):
    print(indice)
    print(aluno)

print("-" * 30)
notas = [8, 7, 7.5, 8.2, 9, 10, 2.5, 6.6, 7.2, 9, 9.2, 7.4]
for nota, aluno in zip(notas, alunos):
    print("Aluno", aluno, "- nota", nota)

alunos.append("k")
print(alunos)

print(alunos.pop())
print(alunos)

# Ordena a lista, passando o resultado para outra variável
notas_ord = sorted(notas)
print(notas)
print(notas_ord)

# Ordena a lista in-place, ou seja, modifica a própria lista
notas.sort()
print(notas)

# Ordena de forma decrescente
notas.sort(reverse=True)
print(notas)
print("-" * 30)

x = 2
y = x
print(x, y)

x = 3
print(x, y)

x = [2]
y = x
print(x, y)

x.append(3)
print(x, y)

def aumenta_lista(nova_lista, valor):
    nova_lista.append(valor)
    return nova_lista

x = []
y = aumenta_lista(x, 10)
print(x, y) # [], [10]

def aumenta_lista2(nova_lista, valor):
    lista = nova_lista.copy()
    lista.append(valor)
    return lista

y = aumenta_lista2(x, 10)
print(x, y) # [10], [10, 10]

def soma_2(lista):
    for ind, elem in enumerate(lista):
        lista[ind] = elem + 2

soma_2(y)
print(y)

def cria_lista(lista_original=None):
    if lista_original is None:
        lista_original = []
    lista_original.append("olá")
    return lista_original

x = cria_lista()
print(x)
y = cria_lista()
print(y)

# Pythonico
# Compreensão de lista
print("-" * 30)
x = [1, 2, 3, 4, 5, 6]
y = []
for num in x:
    y.append(num ** 2)

print(y)

y = [num ** 2 for num in x if num % 2 == 1]
print(y)

# Linearização de matrizes
print(coordenadas)
coord_linear = [a for b in coordenadas for a in b if a != 6]
print(coord_linear)

coord_linear = []
for b in coordenadas:
    for a in b:
        if a != 6:
            coord_linear.append(a)
print(coord_linear)

# Tuplas -> estrutura de dados imutável
print("-" * 30)
coord_rj = (10, 50)
print(coord_rj[0])
print(coord_rj[1:])
# coord_rj[1] = 55 -> TypeError

def le_notas():
    ap1 = float(input())
    ap2 = float(input())
    asub = float(input())
    ac = float(input())
    return ap1, ap2, asub, ac

notas = le_notas()
print(notas)
