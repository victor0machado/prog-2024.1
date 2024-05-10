import random

from .monstro import Monstro

class Boss(Monstro):
    def __init__(self):
        self.nome = "Boss"
        self.vida = random.randint(80, 120)
        self.forca = random.randint(15, 30)
        self.defesa = random.randint(1, 10)
        print("O boss do mapa apareceu!")

    def defender(self, dano):
        dano_levado = dano - self.defesa
        if dano_levado > 0:
            self.vida -= dano_levado
