"""
Programação Estruturada
2024.1
17/04/2024

Bibliotecas e pacotes em Python
"""
import time
import random
from random import randint as rint
from pprint import pprint

import pygame

print(random.randint(2, 10))
print(rint(2, 10))

alunos = [
    {
        "matrícula": 1234,
        "nome": "zé",
        "curso": "ec"
    },
    {
        "matrícula": 5678,
        "nome": "ana",
        "curso": "ads"
    }
]
print(alunos)
pprint(alunos, indent=4)

pop = [1, 2, 7, 4, 5, 6, 3, 8]
print(random.choices(pop, k=4))
print(random.sample(pop, k=4))

pop2 = pop.copy()

random.shuffle(pop2)
print(pop2)
print(pop)

pop3 = pop.copy()
while True:
    num = random.choice(pop3)
    if num < 5:
        break
    pop3.remove(num)

print(num)

def fatorial(num: int) -> int:
    fat: int = 1
    for i in range(1, num + 1):
        fat *= i

    return fat

inicio = time.time()
fatorial(10000)
print(f"Tempo decorrido: {time.time() - inicio} segundos")

time.sleep(2)
print("acabou")
