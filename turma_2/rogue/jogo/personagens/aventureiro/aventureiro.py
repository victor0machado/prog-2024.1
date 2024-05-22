import os.path
import random

from ...mecanicas import som

import pygame

class Aventureiro:
    def __init__(self, nome):
        self.forca = random.randint(10, 18)
        self.defesa = random.randint(10, 18)
        self.vida = random.randint(100, 120)
        self.posicao = [0, 0]
        self.char = "@"
        self.nome = nome
        self.status = "Comece a explorar"

        self.xp_por_nivel = 5
        self.xp = 0
        self.nivel = 1

    def ganhar_xp(self, xp_ganho):
        self.xp += xp_ganho
        if self.xp >= self.xp_por_nivel:
            self.xp -= self.xp_por_nivel
            self.xp_por_nivel += 1
            return True
        return False

    @staticmethod
    def morrer():
        morte = pygame.mixer.Sound(os.path.join(som.DIRETORIO, "morte.wav"))
        pygame.mixer.Sound.play(morte)

    def subir_nivel(self):
        levelup = pygame.mixer.Sound(os.path.join(som.DIRETORIO, "levelup.wav"))
        pygame.mixer.Sound.play(levelup)
        self.nivel += 1
        self.vida += 10
        self.forca += 1
        self.defesa += 1

    def calcular_pos_futura(self, direcao):
        x, y = self.posicao
        match direcao:
            case "W":
                y -= 1
            case "S":
                y += 1
            case "A":
                x -= 1
            case "D":
                x += 1

        return [x, y]

    def andar(self, nova_posicao):
        self.posicao = nova_posicao

    def atacar(self):
        """
        Retorna um inteiro igual à Força do aventureiro, mais um valor aleatório
        entre 1 e 6.
        """
        return self.forca + random.randint(1, 6)

    def defender(self, dano):
        """
        Calcula o dano a ser absorvido pelo aventureiro, igual ao dano causado
        menos o atributo de defesa do aventureiro.

        Se o dano a ser absorvido é menor ou igual a zero, não faz nada. Se for
        maior que zero, reduz esse dano da vida do aventureiro.
        """
        dano_levado = dano - self.defesa
        if dano_levado > 0:
            self.vida -= dano_levado

    def ver_atributos(self):
        """
        Exibe na tela os atributos do aventureiro (nome, vida, força, defesa).
        """
        print("Informações de ", self.nome, ":", sep="")
        print("Vida:", self.vida)
        print("Força:", self.forca)
        print("Defesa:", self.defesa)

    def esta_vivo(self):
        """
        Retorna True se a vida do aventureiro é maior que zero.
        """
        return self.vida > 0
