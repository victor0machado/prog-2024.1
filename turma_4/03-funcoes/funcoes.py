"""
Programação Estruturada
2024.1
01/03/2024

Funções
- Encapsular uma informação
    - Isolar o comportamento para facilitar o uso
- Organizar o código
"""

CAMINHO_DO_PROJETO = "C:\\projetos"

def traco(sep, tamanho):
    print(sep * tamanho)

# Declaração / definição de função
def cabecalho(titulo, sep="-", tamanho=30):
    traco(sep, tamanho)
    print(titulo)
    traco(sep, tamanho)

# Chamando uma função
cabecalho("Relatório de despesas")
cabecalho("Folha de pagamento", tamanho=25, sep=".")

# Não colocar os parênteses significa que estou
# falando da função, e não chamando
print(cabecalho)
print(cabecalho("olá", tamanho=25))

# Toda função tem um retorno
print(print("olá, mundo"))
# print(input("nome: "))

def soma(a, b):
    return a + b

print(soma(2, 5) + soma(4, 9))

x = 2
print(x % 2 == 0)

def e_par(num):
    return num % 2 == 0

print(e_par(8))
print(e_par(55))

def troca_valores(a, b):
    return b, a # esse retorno é uma tupla

print(troca_valores(8, 0))
y = 5

x, y = troca_valores(x, y)
print(x, y)

# Escopo de variáveis
def func1():
    a = 10
    print(a) # escopo local
    print(x) # escopo global

print("-" * 30)
func1()

def func2(x):
    x = 999
    print(x) # escopo local tem preferência

func2(100)
print(x)

def func3():
    global x  # NÃO USAR!!!!!!
    x = 0
    print(x)

func3()
print(x) # 0

def func4():
    print(CAMINHO_DO_PROJETO)

func4()
