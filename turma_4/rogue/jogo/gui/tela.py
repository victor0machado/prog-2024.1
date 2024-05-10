from .cores import CORES

import pygame

GRID = 40

def centralizar_texto(posicao_inicial, texto):
    x0 = posicao_inicial[0] * GRID + (GRID - texto.get_width()) // 2
    y0 = posicao_inicial[1] * GRID + (GRID - texto.get_height()) // 2
    return [x0, y0]

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

    def desenha_mensagem(self, mensagem, posicao):
        fonte = pygame.font.SysFont(None, GRID)
        texto = fonte.render(mensagem, True, CORES.branco)
        self.display.blit(texto, centralizar_texto(posicao, texto))

    def aventureiro(self, aventureiro):
        self.desenha_mensagem("@", aventureiro.posicao)

    def tesouro(self, tesouro):
        self.desenha_mensagem("X", tesouro.posicao)

    def mapa(self, aventureiro, tesouro):
        for linha in range(10):
            for coluna in range(10):
                if [linha, coluna] not in [aventureiro.posicao, tesouro.posicao]:
                    self.desenha_mensagem(".", [linha, coluna])
