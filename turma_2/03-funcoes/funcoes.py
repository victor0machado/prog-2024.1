"""
Programação Estruturada
2024.1
04/03/2024

Funções
- Evitar duplicidade de código
- Organizar melhor o código

Princípios SOLID
SRP - Single Responsibility Principle

Encapsulamento
"""

CAMINHO_DO_PROJETO = "C:\\Projetos"

def traco(largura, caract_traco):
    print(caract_traco * largura)

# def -> definir (ou declarar)
def cabecalho(titulo, largura=30, caract_traco="-"):
    traco(largura, caract_traco)
    print(titulo)
    traco(largura, caract_traco)

# Uso ou chamada da função
cabecalho("Relatório de vendas", largura=30)
cabecalho("Folha de pagamento", 25, caract_traco=".")
print(cabecalho("Lista de fornecedores", caract_traco="="))
print(print("olá"))

"""
Entrada de dados
Processamento
Saída de dados
"""
def soma(a, b):
    return a + b

print(soma(10, 2) + soma(1, 5))

def e_par(num):
    return num % 2 == 0

def subsequentes(num):
    return num + 1, num + 2 # A função retorna uma tupla

x, y = subsequentes(10)
print(subsequentes(10))
print(x, y)

print("-" * 30)
# Escopo de variáveis
x = 0 # escopo global

def func1(x):
    x = 1 # escopo local
    print(x)

def func2():
    x = 2
    print(x)

def func3():
    print(x)

def func4():
    global x # NÃO USAR!!!!!
    x = 4
    print(x)

print(x)
func1(x)
func2()
func3()
func4()
print(x)

# Evitem o uso de variáveis globais
# A não ser que sejam constantes (no início do arquivo)
