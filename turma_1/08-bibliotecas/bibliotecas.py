"""
Programação Estruturada
2024.1
15/04/2024

Bibliotecas, Pacotes e a Biblioteca Padrão do Python

- Módulo: arquivo python
- Pacote: conjunto de módulos
- Biblioteca: conjuntos de pacotes
"""
# import random as rnd
import time

from random import randint as rint
from random import random, choice
from pprint import pprint

import pygame

dicio = {
    "aluno": "Maria",
    "nascimento": "10/10/2000",
    "disciplinas": ["Programação, Cálculo, Estatística"]
}

pprint(dicio, indent=4)

lista = [4, 6, 2, 1, 10]
# lista.sort()
# print(lista)
nova_lista = sorted(lista)
print(lista)
print(nova_lista)

def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i

    return fat

inicio = time.time()
fatorial(10000)
print(f"A função levou {time.time() - inicio} segundos.")
print(time.time())

# time.sleep(2)


