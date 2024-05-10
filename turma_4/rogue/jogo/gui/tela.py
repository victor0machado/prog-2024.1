from .cores import CORES

import pygame

GRID = 40

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((10 * GRID, 10 * GRID))
        pygame.display.set_caption("Rogue")

    def renderizar(self):
        self.display.fill(CORES.preto)

        pygame.display.update()
