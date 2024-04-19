"""
Programação Estruturada
2024.1
19/04/2024

Módulos, Pacotes e Bibliotecas em Python
"""
import time
import random as rnd
from random import randint

import pygame

# NÃO USAR!!!!!!
# from random import *

print(rnd.randint(1, 6))
print(randint(1, 6))

# texto = input()

lista = [1, 2, 3, 4, 5, 6]
outra_lista = lista.copy()
rnd.shuffle(outra_lista)

print(lista)
print(outra_lista)

def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i

    return fat

inicio = time.time()
fatorial(1000)
print(f"Tempo decorrido: {time.time() - inicio:.2f} segundos.")

time.sleep(3)
print("acabou")
