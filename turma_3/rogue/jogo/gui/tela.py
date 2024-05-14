from .cores import CORES

import pygame

GRID = 40
LARGURA = 10 * GRID
ALTURA = 10 * GRID
FONTE = "Courier New"

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")

    def renderizar(self, aventureiro, tesouro):
        self.display.fill(CORES.preto)
        pygame.display.update()
