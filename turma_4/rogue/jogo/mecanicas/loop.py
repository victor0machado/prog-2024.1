from jogo.gui.tela import Tela

from . import movimento
from . import inputbox

from jogo.personagens.monstros.boss import Boss
from jogo.personagens.aventureiro import Aventureiro
from jogo.personagens.tesouro import Tesouro

import pygame

def jogo():
    aventureiro = Aventureiro()
    tesouro = Tesouro()

    nome = inputbox.ler_texto("Informe o seu nome:")
    aventureiro.nome = nome
    print(f"Saudações, {aventureiro.nome}! Boa sorte!")

    tela = Tela()

    mensagem_combate = ""
    jogo_acabou = False
    while not jogo_acabou:
        # Controlar os eventos
        teclas = pygame.key.get_pressed()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

            if evento.type == pygame.KEYUP:
                if teclas[pygame.K_q]:
                    print("Já correndo?")
                    return

                if teclas[pygame.K_z]:
                    aventureiro.mudar_cor()
                elif teclas[pygame.K_x]:
                    aventureiro.mudar_char()
                elif teclas[pygame.K_KP_PLUS]:
                    aventureiro.aumentar_dificuldade()
                elif teclas[pygame.K_KP_MINUS]:
                    aventureiro.diminuir_dificuldade()
                else:
                    # Executar as ações do jogo
                    resultado, nome_monstro = movimento.movimentar(aventureiro, teclas)
                    if resultado == 0:
                        mensagem_combate = f"Você foi derrotado por {nome_monstro}..."
                        jogo_acabou = True
                    elif resultado == 1:
                        mensagem_combate = f"{nome_monstro} foi derrotado!"
                    else:
                        mensagem_combate = "Você não encontrou nada"

                    if aventureiro.posicao == tesouro.posicao:
                        boss = Boss(aventureiro.dificuldade)
                        if movimento.iniciar_combate(aventureiro, boss):
                            mensagem_combate = f"Parabéns, {aventureiro.nome}, você encontrou o tesouro!"
                        else:
                            mensagem_combate = f"Você foi derrotado pelo chefão... =("

                        jogo_acabou = True

        # Desenho na tela
        tela.renderizar(aventureiro, tesouro, mensagem_combate)

        # Chamar o relógio interno do jogo
        pygame.time.Clock().tick(60)
