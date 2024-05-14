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
        self.personagem(aventureiro)
        self.personagem(tesouro)

        pygame.display.update()

    def personagem(self, personagem):
        # fonte
        fonte = pygame.font.SysFont(FONTE, GRID)
        # renderização do texto
        texto = fonte.render(personagem.char, True, CORES.branco)
        # inserir o render na tela
        x = personagem.posicao[0] * GRID
        y = personagem.posicao[1] * GRID
        self.display.blit(texto, [x, y])
