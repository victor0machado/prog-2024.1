from .cores import CORES

import pygame

GRID = 40

def centralizar_grid(posicao, texto):
    return [
        posicao[0] * GRID + (GRID - texto.get_width()) // 2,
        posicao[1] * GRID + (GRID - texto.get_height()) // 2,
    ]

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((10 * GRID, 10 * GRID))
        pygame.display.set_caption("Rogue")

    def renderizar(self, aventureiro, tesouro):
        self.display.fill(CORES.preto)
        self.aventureiro(aventureiro)
        self.tesouro(tesouro)
        self.mapa(aventureiro, tesouro)

        pygame.display.update()

    def escreve_grid(self, mensagem, posicao):
        fonte = pygame.font.SysFont(None, GRID)
        texto = fonte.render(mensagem, True, CORES.branco)
        self.display.blit(texto, centralizar_grid(posicao, texto))

    def aventureiro(self, aventureiro):
        self.escreve_grid("@", aventureiro.posicao)

    def tesouro(self, tesouro):
        self.escreve_grid("X", tesouro.posicao)

    def mapa(self, aventureiro, tesouro):
        for linha in range(10):
            for coluna in range(10):
                if [linha, coluna] not in [aventureiro.posicao, tesouro.posicao]:
                    self.escreve_grid(".", [linha, coluna])

