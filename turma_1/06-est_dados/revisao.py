x = 2
y = x
print(x, y) # 2 2

x = 3
print(x, y) # 3 2

x = [2]
y = x
print(x, y) # [2] [2]

# Passagem por referência
x.append(3)
print(x, y) # [2, 3] [2, 3]

def func1(a):
    a.append(2)

func1(x)
print(x) # [2, 3, 2]

def func2(a):
    b = a.copy() # shallow copy
    b.append(2)
    return b

y = func2(x)
print(x, y) # [2, 3, 2] [2, 3, 2, 2]

# Evitar o uso de dados não primitivos em parâmetros-chave
def atualiza_lista(lista=[]):
    lista.append(2)
    return lista

x = atualiza_lista()
print(x)

x = atualiza_lista()
print(x)

def atualiza_lista2(lista=None):
    if lista is None:
        lista = []
    lista.append(2)
    return lista

x = atualiza_lista2()
print(x)

x = atualiza_lista2()
print(x)

def adiciona_nota_aluno(dic, matricula, nota):
    dic[matricula] = nota

alunos = {}
adiciona_nota_aluno(alunos, "1234", 7.5)
adiciona_nota_aluno(alunos, "5678", 8.8)
print(alunos)

def func3(dic):
    dic["4"] = 4.5

def func4(dic):
    dic["5"] = 7.5

def calcula_notas():
    notas = {}
    func3(notas)
    func4(notas)

def op1():
    print("Operação 1")

def op2():
    print("Operação 2")

def op3():
    print("Operação 3")

def erro():
    print("Erro")

opcoes = {
    "1": op1,
    "2": op2,
    "3": op3,
    "0": exit
}

def main():
    while True:
        opcao = input("Informe a operação desejada: ")
        opcoes.get(opcao, erro)()

# main()

# Compreensão de listas (list comprehension)
numeros = [1, 2, 3, 4, 5, 6, 7]

# quadrados = []
# for numero in numeros:
#     quadrados.append(numero ** 2)
quadrados = [numero ** 2 for numero in numeros]

print(quadrados)

quadrados_impares = [numero ** 2 for numero in numeros if numero % 2 == 1]
print(quadrados_impares)

matriz = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10]
]
linha_completa = []
for linha in matriz:
    for elemento in linha:
        linha_completa.append(elemento)

print(linha_completa)

# Usar o bom senso na hora de compreensão de listas
# Por exemplo, evitar o caso abaixo:
linha_completa = [elem for linha in matriz for elem in linha]
print(linha_completa)
