from .mecanicas import movimentar

from ..personagens.aventureiro import Aventureiro
from ..personagens.tesouro import Tesouro
from ..gui.tela import Tela

import pygame

def executar():
    """
    Fluxo principal do jogo, possui as seguintes etapas:
    - Instancia um aventureiro
    - Instancia um tesouro
    - Desenha o mapa pela primeira vez
    - Em um loop infinito:
        - Lê o comando inserido pelo usuário
        - Se for o comando "Q", encerra o programa
        - Se for o comando "T", exibe os atributos do aventureiro
        - Se o comando for "W", "A", "S" ou "D":
            - Realiza o movimento e verifica o resultado da função movimentar
            - Se o resultado for True, desenha novamente o mapa
            - Se for False, imprime "Game over" na tela e encerra o programa
        - Se o usuário inserir algum comando diferente, diz que não reconheceu
        - Se a posição do aventureiro for igual à posição do tesouro, dispara
        uma mensagem que o aventureiro ganhou o jogo
    """
    aventureiro = Aventureiro()
    tesouro = Tesouro()
    tela = Tela()

    print(f"Saudações, {aventureiro.nome}! Boa sorte!")

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_q]:
            print("Já correndo?")
            return

        if teclas[pygame.K_t]:
            print(aventureiro)

        if not movimentar(aventureiro, teclas):
            print("Game Over")
            return

        tela.renderizar(aventureiro, tesouro)
        pygame.time.Clock().tick(60)

        if aventureiro.posicao == tesouro.posicao:
            print(f"Parabéns, {aventureiro.nome}! Você encontrou o tesouro!")
            return
