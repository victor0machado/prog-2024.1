import random

from .monstro import Monstro

class Thanos(Monstro):
    def __init__(self):
        self.nome = "Thanos"
        self.vida = random.randint(10, 100)
        self.forca = random.randint(15, 25)
        print("Um Thanos apareceu!")

    def atacar(self):
        return self.forca + random.randint(1, 4)
