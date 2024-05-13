from .cores import CORES
from .relogio import relogio

import pygame

GRID = 40
TAM_MAPA = 10
LARGURA = GRID * TAM_MAPA + 400
ALTURA = GRID * TAM_MAPA + 100
MARGEM = 10
FONTE = "Lucida Console"

TEXTOS_FIM_JOGO = {
    "Você foi derrotado...": "Derrota",
    "Parabéns! Você encontrou o tesouro!": "Vitória"
}

def centralizar_grid(posicao, texto):
    x = posicao[0] * GRID + (GRID - texto.get_width()) // 2
    y = posicao[1] * GRID + (GRID - texto.get_height()) // 2
    return [x + (LARGURA - GRID * TAM_MAPA) // 2, y + (ALTURA - GRID * TAM_MAPA) // 2]

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")

    def renderizar(self, aventureiro, tesouro, mensagem_combate, obstaculos):
        self.display.fill(CORES.preto)
        self.aventureiro(aventureiro)
        self.tesouro(tesouro)
        self.mapa(aventureiro, tesouro, obstaculos)
        self.combate(mensagem_combate)
        self.obstaculos(obstaculos)
        self.relogio()

        if mensagem_combate in TEXTOS_FIM_JOGO.keys():
            self.fim_jogo(mensagem_combate)

        pygame.display.update()

    def fim_jogo(self, mensagem_combate):
        fonte = pygame.font.SysFont(FONTE, GRID * 2)
        texto = fonte.render(TEXTOS_FIM_JOGO[mensagem_combate], True, CORES.vermelho, CORES.branco)
        self.display.blit(
            texto,
            [(LARGURA - texto.get_width()) // 2, (ALTURA - texto.get_height()) // 2]
        )

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

    def obstaculos(self, obstaculos):
        for obstaculo in obstaculos:
            self.escreve_grid("O", obstaculo.posicao)

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

    def mapa(self, aventureiro, tesouro, obstaculos):
        for linha in range(10):
            for coluna in range(10):
                posicoes_invalidas = [aventureiro.posicao, tesouro.posicao]
                for obstaculo in obstaculos:
                    posicoes_invalidas.append(obstaculo.posicao)
                if [linha, coluna] not in posicoes_invalidas:
                    self.escreve_grid(".", [linha, coluna])

