from .cores import CORES

import pygame

GRID = 40
LARGURA = 10 * GRID
ALTURA = 10 * GRID
FONTE = "Courier New"

def centralizar_grid(texto, posicao_inicial):
    x = posicao_inicial[0] + (GRID - texto.get_width()) // 2
    y = posicao_inicial[1] + (GRID - texto.get_height()) // 2
    return [x, y]

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")
        self.fonte = pygame.font.SysFont(FONTE, GRID)

    def renderizar(self, aventureiro, tesouro):
        self.display.fill(CORES.preto)
        self.personagem(aventureiro)
        self.personagem(tesouro)
        self.mapa(aventureiro, tesouro)

        pygame.display.update()

    def mapa(self, aventureiro, tesouro):
        texto = self.fonte.render(".", True, CORES.branco)
        for linha in range(10):
            for coluna in range(10):
                if [linha, coluna] not in [aventureiro.posicao, tesouro.posicao]:
                    self.display.blit(texto, centralizar_grid(texto, [linha * GRID, coluna * GRID]))

    def personagem(self, personagem):
        # renderização do texto
        texto = self.fonte.render(personagem.char, True, CORES.branco)
        # inserir o render na tela
        x = personagem.posicao[0] * GRID
        y = personagem.posicao[1] * GRID
        self.display.blit(texto, centralizar_grid(texto, [x, y]))
