from .mecanicas import movimentar

from ..personagens.aventureiro import Aventureiro
from ..personagens.tesouro import Tesouro
from ..personagens.obstaculo import Obstaculos
from ..gui.tela import Tela
from ..gui.input_texto import InputBox

import pygame

TOTAL_OBSTACULOS = 5

def input_box():
    inputbox = InputBox("Olá! Informe o seu nome:")

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return inputbox.texto

            texto = inputbox.tratar_eventos(evento)
            if texto is not None:
                return texto

        inputbox.renderizar()

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
    obstaculos = Obstaculos(TOTAL_OBSTACULOS, tesouro)
    aventureiro.nome = input_box()

    tela = Tela()
    print(f"Saudações, {aventureiro.nome}! Boa sorte!")

    primeiro_movimento = True
    jogo_encerrou = False
    while not jogo_encerrou:
        teclas = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

            if evento.type == pygame.KEYUP:
                if teclas[pygame.K_q]:
                    print("Já correndo?")
                    return

                if not primeiro_movimento:
                    aventureiro.status = "Continue explorando"
                primeiro_movimento = False

                resultado_movimento = movimentar(aventureiro, teclas, obstaculos)
                if resultado_movimento == 0:
                    aventureiro.fim_jogo = False
                    jogo_encerrou = True
                elif resultado_movimento == 2:
                    aventureiro.causar_dano_veneno()
                    if not aventureiro.esta_vivo():
                        aventureiro.status = "Você foi morto por veneno..."
                        aventureiro.fim_jogo = False
                        jogo_encerrou = True
                    elif aventureiro.posicao == tesouro.posicao:
                        aventureiro.status = "Parabéns! Você encontrou o tesouro!"
                        aventureiro.fim_jogo = True
                        jogo_encerrou = True

        tela.renderizar(aventureiro, tesouro, obstaculos.obstaculos)
        pygame.time.Clock().tick(60)
