"""
Programação Estruturada
2024.1
08/03/2024

Funções
- Encapsulamento
    - Evitar ao máximo duplicidade de código
- Organização do código
"""

PI = 3.14
CAMINHO_DO_PROJETO = "C:\\Projetos"

def linha(largura, traco):
    print(traco * largura)

def cabecalho(titulo, largura=30, traco="."):
    linha(largura, traco)
    print(titulo)
    linha(largura, traco)

cabecalho("Folha de pagamento", 30)
cabecalho("Lista de fornecedores", 25)
cabecalho("DEMONSTRATIVO DE RESULTADOS", traco="=")

# Não é chamar a função, é indicar a referência da função
cabecalho
print(cabecalho)

def soma(a, b):
    return a + b

print(soma(4, 8) + soma(2, -5))

# Múltiplos retornos
def subsequentes(a):
    return a + 1, a + 2 # tupla

a, b = subsequentes(10)
print(a, b)
print(subsequentes(5))

# Escopo de variáveis
print("-" * 30)

def func(x):
    x = 1 # escopo local
    print(x)

def func2():
    x = 2
    print(x)

def func3():
    global x # NÃO USAR!!!!!!
    x = 3
    print(x)

def func4():
    print(x)

# escopo global
# sempre que possível, devemos evitar variáveis de escopo global
x = 0

print(x)
func(x)
func2()
func3()
func4()
print(x)
