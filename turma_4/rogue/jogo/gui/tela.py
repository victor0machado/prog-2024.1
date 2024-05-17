from .cores import CORES

import pygame

GRID = 40
TAMANHO_MAPA = 10

LARGURA_ADICIONAL = 500
ALTURA_ADICIONAL = 100
MARGEM = 10

FONTE = "Courier New"

def centralizar_texto_mapa(posicao_inicial, texto):
    x0 = posicao_inicial[0] * GRID + (GRID - texto.get_width()) // 2
    y0 = posicao_inicial[1] * GRID + (GRID - texto.get_height()) // 2
    return [x0 + LARGURA_ADICIONAL // 2, y0 + ALTURA_ADICIONAL // 2]

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode(
            (TAMANHO_MAPA * GRID + LARGURA_ADICIONAL, TAMANHO_MAPA * GRID + ALTURA_ADICIONAL)
        )
        pygame.display.set_caption("Rogue")

    def renderizar(self, aventureiro, tesouro, mensagem_combate):
        self.display.fill(CORES.preto)
        self.aventureiro(aventureiro)
        self.tesouro(tesouro)
        self.mapa(aventureiro, tesouro)
        self.combate(mensagem_combate)

        pygame.display.update()

    def combate(self, mensagem_combate):
        fonte = pygame.font.SysFont(FONTE, GRID // 2)
        texto = fonte.render(mensagem_combate, True, CORES.branco)
        self.display.blit(texto, [MARGEM, MARGEM])

    def desenha_mensagem(self, mensagem, posicao, cor=CORES.branco):
        fonte = pygame.font.SysFont(FONTE, GRID)
        texto = fonte.render(mensagem, True, cor)
        self.display.blit(texto, centralizar_texto_mapa(posicao, texto))

    def aventureiro(self, aventureiro):
        self.desenha_mensagem(aventureiro.char, aventureiro.posicao, aventureiro.cor)

        atributos = f"{aventureiro.nome} nv. {aventureiro.nivel} ({aventureiro.xp}/{aventureiro.xp_por_nivel}): " \
            f"vida {aventureiro.vida}; força {aventureiro.forca}; defesa {aventureiro.defesa}"

        fonte = pygame.font.SysFont(FONTE, GRID // 2)
        texto = fonte.render(atributos, True, CORES.branco)

        y = GRID * TAMANHO_MAPA + ALTURA_ADICIONAL - MARGEM - texto.get_height()
        self.display.blit(texto, [MARGEM, y])

    def tesouro(self, tesouro):
        self.desenha_mensagem("X", tesouro.posicao)

    def mapa(self, aventureiro, tesouro):
        for linha in range(TAMANHO_MAPA):
            for coluna in range(TAMANHO_MAPA):
                if [linha, coluna] not in [aventureiro.posicao, tesouro.posicao]:
                    self.desenha_mensagem(".", [linha, coluna])
