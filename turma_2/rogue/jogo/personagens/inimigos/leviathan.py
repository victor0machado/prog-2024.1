import random

from .inimigo import Inimigo

class Leviathan(Inimigo):
    def __init__(self):
        self.forca = random.randint(20, 40)
        self.vida = random.randint(80, 200)
        self.xp = 8
        self.nome = "Leviathan"
