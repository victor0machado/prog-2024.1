"""
Programação Estruturada
2024.1
27/02/2024

Funções
"""

CAMINHO_DO_PROJETO = "C:\\Projetos"

def linha_cabecalho(largura, sep):
    print(sep * largura)

def cabecalho(titulo, largura=30, sep="-"):
    linha_cabecalho(largura, sep)
    print(titulo)
    linha_cabecalho(largura, sep)

print("Teste")

cabecalho("Relatório de Compras", 30)
cabecalho("Resumo Operacional", 25)
cabecalho("Portfólio de clientes")
cabecalho("Lista de funcionários", sep="=", largura=15)

def soma(a, b):
    return a + b

total_valores = soma(5, 7) + soma(1, 9)

def e_par(num):
    return num % 2 == 0

print(e_par(18))
print(e_par(7))

def troca_valores(x, y):
    return y, x

a, b = troca_valores(10, 20)
print(a, b)

# Escopo de variáveis
# Como boa prática, não vamos declarar variáveis fora de funções
print("-" * 30)
def func1(x):
    x = 5
    print(x)

def func2(x):
    x += 2
    print(x)

x = 1
func1(x)
func2(x)
print(x)

def func3():
    print(x)

func3()

def func4():
    x = 5
    print(x)

func4()
print(x)

def func5():
    global x # NÃO USAR!!!!!
    x = 5
    print(x)

func5()
print(x)
