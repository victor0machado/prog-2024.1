from .cores import CORES

import pygame

GRID = 40
LARGURA = 10 * GRID + 350
ALTURA = 10 * GRID + 100
MARGEM = 10
FONTE = "Courier New"

def centralizar_grid(texto, posicao_inicial):
    x = (LARGURA - 10 * GRID) // 2 + posicao_inicial[0] + (GRID - texto.get_width()) // 2
    y = (ALTURA - 10 * GRID) // 2 + posicao_inicial[1] + (GRID - texto.get_height()) // 2
    return [x, y]

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")
        self.fonte_grid = pygame.font.SysFont(FONTE, GRID)
        self.fonte_msg = pygame.font.SysFont(FONTE, GRID // 2)

    def renderizar(self, aventureiro, tesouro):
        self.display.fill(CORES.preto)
        self.personagem(aventureiro, aventureiro.cor)
        self.personagem(tesouro)
        self.atributos(aventureiro)
        self.status(aventureiro.status)
        self.mapa(aventureiro, tesouro)

        pygame.display.update()

    def status(self, mensagem):
        texto = self.fonte_msg.render(mensagem, True, CORES.branco)
        self.display.blit(texto, [MARGEM, MARGEM])

    def atributos(self, aventureiro):
        mensagem = f"{aventureiro.nome} nv {aventureiro.nivel}: " \
            f"Vida {aventureiro.vida} - Força {aventureiro.forca} - Defesa {aventureiro.defesa}"
        texto = self.fonte_msg.render(mensagem, True, CORES.branco)
        self.display.blit(texto, [MARGEM, ALTURA - MARGEM - texto.get_height()])

    def mapa(self, aventureiro, tesouro):
        texto = self.fonte_grid.render(".", True, CORES.branco)
        for linha in range(10):
            for coluna in range(10):
                if [linha, coluna] not in [aventureiro.posicao, tesouro.posicao]:
                    self.display.blit(texto, centralizar_grid(texto, [linha * GRID, coluna * GRID]))

    def personagem(self, personagem, cor=CORES.branco):
        # renderização do texto
        texto = self.fonte_grid.render(personagem.char, True, cor)
        # inserir o render na tela
        x = personagem.posicao[0] * GRID
        y = personagem.posicao[1] * GRID
        self.display.blit(texto, centralizar_grid(texto, [x, y]))
