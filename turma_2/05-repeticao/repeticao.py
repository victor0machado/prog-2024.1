"""
Programação Estruturada
2024.1
13/03/2024

Estruturas de Repetição
- while -> quando não sabemos quantas vezes vamos executar a
repetição
- for -> quando queremos acessar todos os elementos de uma
coleção de dados
"""

def contagem_regressiva(num):
    while num >= 0:
        print(num)
        num -= 1 # num = num - 1

contagem_regressiva(5)
print("-" * 30)

# Evitar loops infinitos
def contagem_regressiva2(num):
    while num >= 0:
        print(num)

# contagem_regressiva2(5)
# print("-" * 30)

print(list(range(5)))
print(list(range(2, 5)))
print(list(range(1, 11, 2)))
print(list(range(10, -5, 2)))
print(list(range(-10, 5, -2)))

def contagem_regressiva3(num):
    for cont in range(num, -1, -1):
        print(cont)

contagem_regressiva3(5)
print("-" * 30)

def ola_varias_vezes(num):
    for _ in range(num):
        print("olá")

ola_varias_vezes(5)
print("-" * 30)

def le_nomes():
    texto = "1"
    while texto != "":
        texto = input("Informe o seu nome, ou digite um número: ")
        if texto.isnumeric():
            continue # interrompe o loop atual
        print(texto)

# le_nomes()

def le_nome():
    while True:
        nome = input("Informe o seu nome: ")
        if nome:
            break # interrompe a estrutura de repetição

    print(nome)

# le_nome()

def e_primo(num):
    for div in range(2, num):
        if not num % div:
            print(num, "não é primo.")
            break
    else: # só entra no else se não rodar o break
        print(num, "é primo.")

    print("fim da função")

e_primo(7)
e_primo(8)
e_primo(31)
e_primo(56)
