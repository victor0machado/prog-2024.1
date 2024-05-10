import random

from .monstro import Monstro

class Demogorgon(Monstro):
    def __init__(self):
        self.nome = "Demogorgon"
        self.vida = random.randint(80, 120)
        self.forca = random.randint(5, 25)
        print("Um Demogorgon apareceu!")
