import random # -> ideal
# from random import randint as rint
# import numpy as np
# import pandas as pd

# wildcard - !!!!NÃO USAR!!!!
# from random import *

print(random.randint(1, 10))
# print(rint(1, 10))
# print(choice([1, 2, 3, 4]))

# texto = input()

# print(texto.isnumeric())

import time

def fatorial(n : int) -> int:
    fat : int = 1
    for i in range(1, n + 1):
        fat *= i

    return fat

fatorial(5) # 120

inicio = time.time()
fatorial(10)
fim = time.time()

print(f"Tempo decorrido: {fim - inicio} segundos.")

# time.sleep(3)

print("oi")

aluno = {
    "nome": "zé",
    "matricula": "12345",
    "data_nascimento": "10/10/2000",
    "idade": 20,
    "disciplinas": {
        "disc1": "programação",
        "disc2": "cálculo"
    }
}

print(aluno)

from pprint import pprint

pprint(aluno, indent=4, depth=1)

lista = [1, 2, 3, 4, 5, 6]
print(random.choices(lista, k=5))
print(random.sample(lista, k=5))

outra_lista = lista.copy()
random.shuffle(outra_lista)
print(lista)
print(outra_lista)

print("C:\Projetos\programação")
print("/usr/projetos/prog")

import pygame
