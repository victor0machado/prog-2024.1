"""
Reune funções de operações aritméticas.
"""
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

if __name__ == "__main__":
    assert 5 == soma(2, 3)
    print("sucesso no teste")
