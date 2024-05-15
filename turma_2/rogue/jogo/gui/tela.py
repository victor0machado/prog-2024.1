from .cores import CORES

import pygame

GRID = 40
MARGEM = 10
LARGURA = GRID * 10 + 200
ALTURA = GRID * 10 + 100
FONTE = "Courier New"

def centralizar_texto(texto, posicao_original):
    x = posicao_original[0] + (LARGURA - 10 * GRID) // 2 + (GRID - texto.get_width()) // 2
    y = posicao_original[1] + (ALTURA - 10 * GRID) // 2 + (GRID - texto.get_height()) // 2
    return [x, y]

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")

    def renderizar(self, aventureiro, tesouro):
        self.display.fill(CORES.preto)
        self.aventureiro(aventureiro)
        self.tesouro(tesouro)
        self.mapa(aventureiro, tesouro)
        pygame.display.update()

    def mapa(self, aventureiro, tesouro):
        fonte = pygame.font.SysFont(FONTE, GRID)
        texto = fonte.render(".", True, CORES.branco)
        for linha in range(10):
            for coluna in range(10):
                if [linha, coluna] not in [aventureiro.posicao, tesouro.posicao]:
                    self.display.blit(texto, centralizar_texto(texto, [linha * GRID, coluna * GRID]))

    def tesouro(self, tesouro):
        fonte = pygame.font.SysFont(FONTE, GRID)
        texto = fonte.render("X", True, CORES.branco)
        self.display.blit(
            texto,
            centralizar_texto(texto, [GRID * tesouro.posicao[0], GRID * tesouro.posicao[1]])
        )

    def aventureiro(self, aventureiro):
        # definição da fonte
        fonte = pygame.font.SysFont(FONTE, GRID)
        # renderização do texto
        texto = fonte.render("@", True, CORES.branco)
        # inserção do render na tela
        self.display.blit(
            texto,
            centralizar_texto(texto, [GRID * aventureiro.posicao[0], GRID * aventureiro.posicao[1]])
        )

        fonte = pygame.font.SysFont(FONTE, GRID // 2)
        atributos = f"{aventureiro.nome}: " \
            f"Vida: {aventureiro.vida} / Força: {aventureiro.forca} / Defesa: {aventureiro.defesa}"
        texto = fonte.render(atributos, True, CORES.branco)
        self.display.blit(texto, [MARGEM, ALTURA - MARGEM - texto.get_height()])
