from .cores import CORES
from .relogio import relogio

import pygame

GRID = 40
TAM_MAPA = 10
LARGURA = GRID * TAM_MAPA + 400
ALTURA = GRID * TAM_MAPA + 100
MARGEM = 10
FONTE = "Courier New"

def centralizar_grid(posicao, texto):
    x = posicao[0] * GRID + (GRID - texto.get_width()) // 2
    y = posicao[1] * GRID + (GRID - texto.get_height()) // 2
    return [x + (LARGURA - GRID * TAM_MAPA) // 2, y + (ALTURA - GRID * TAM_MAPA) // 2]

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")

    def renderizar(self, aventureiro, tesouro, mensagem_combate):
        self.display.fill(CORES.preto)
        self.aventureiro(aventureiro)
        self.tesouro(tesouro)
        self.mapa(aventureiro, tesouro)
        self.combate(mensagem_combate)
        self.relogio()

        pygame.display.update()

    def relogio(self):
        fonte = pygame.font.SysFont(FONTE, GRID // 2)
        texto = fonte.render(relogio.medir_tempo(), True, CORES.branco)
        self.display.blit(texto, [LARGURA - MARGEM - texto.get_width(), MARGEM])

    def combate(self, mensagem):
        fonte = pygame.font.SysFont(FONTE, GRID // 2)
        texto = fonte.render(mensagem, True, CORES.branco)
        self.display.blit(texto, [MARGEM, MARGEM])

    def escreve_grid(self, mensagem, posicao):
        fonte = pygame.font.SysFont(FONTE, GRID)
        texto = fonte.render(mensagem, True, CORES.branco)
        self.display.blit(texto, centralizar_grid(posicao, texto))

    def aventureiro(self, aventureiro):
        self.escreve_grid("@", aventureiro.posicao)

        atributos = f"{aventureiro.nome}" \
            f" nv {aventureiro.nivel}" \
            f" - vida: {aventureiro.vida}/{aventureiro.vida_max};" \
            f" força: {aventureiro.forca};" \
            f" defesa: {aventureiro.defesa}"
        fonte = pygame.font.SysFont(FONTE, GRID // 2)
        texto = fonte.render(atributos, True, CORES.branco)
        self.display.blit(texto, [MARGEM, ALTURA - MARGEM - texto.get_height()])

    def tesouro(self, tesouro):
        self.escreve_grid("X", tesouro.posicao)

    def mapa(self, aventureiro, tesouro):
        for linha in range(10):
            for coluna in range(10):
                if [linha, coluna] not in [aventureiro.posicao, tesouro.posicao]:
                    self.escreve_grid(".", [linha, coluna])

