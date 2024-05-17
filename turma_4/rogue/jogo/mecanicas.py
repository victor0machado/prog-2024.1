import random

from jogo.gui.tela import Tela

from jogo.personagens.monstros.boss import Boss
from jogo.personagens.monstros.thanos import Thanos
from jogo.personagens.monstros.demogorgon import Demogorgon

from jogo.personagens.aventureiro import Aventureiro
from jogo.personagens.tesouro import Tesouro

import pygame

def iniciar_combate(aventureiro, inimigo):
    """
    Executa um loop infinito, que possui as seguintes etapas:
    - Calcula o dano causado pelo aventureiro
    - Monstro faz a sua defesa
    - Exibe na tela o dano causado pelo aventureiro e a vida atual do monstro
    - Se o monstro não está mais vivo, retorna True
    - Calcula o dano causado pelo monstro
    - Aventureiro faz sua defesa
    - Exibe na tela o dano causado pelo monstro e a vida atual do aventureiro
    - Se o aventureiro não está mais vivo, retorna False
    """
    while True:
        dano = aventureiro.atacar()
        inimigo.defender(dano)
        print(f"{aventureiro.nome} causa {dano} de dano! Vida de {inimigo.nome}: {inimigo.vida}")
        if not inimigo.esta_vivo():
            aventureiro.ganhar_xp(inimigo.xp)
            print(f"{inimigo.nome} foi derrotado!")
            return True

        dano = inimigo.atacar()
        aventureiro.defender(dano)
        print(f"{inimigo.nome} causa {dano} de dano! Vida de {aventureiro.nome}: {aventureiro.vida}")
        if not aventureiro.esta_vivo():
            print(f"{aventureiro.nome} foi derrotado!")
            return False

def determina_direcao(teclas):
    if teclas[pygame.K_a]:
        return "A"
    if teclas[pygame.K_w]:
        return "W"
    if teclas[pygame.K_s]:
        return "S"
    if teclas[pygame.K_d]:
        return "D"

    return ""

def movimentar(aventureiro, teclas):
    """
    Realiza a ação de movimento e analisa as consequências.

    Chama a função aventureiro.andar e analisa o seu resultado.

    Em seguida, analisa o efeito do movimento. Há 60% de chance de nada
    acontecer, e 40% de chance de um monstro aparecer (pesquise sobre a função
    random.choices).

    Se um monstro aparecer, inicia um novo monstro e retorna e resultado da
    função iniciar_combate.

    Se não aconteceu nada, retorna 2.
    Se houve um combate o aventureiro foi vitorioso, retorna 1.
    Se houve um combate e o aventureiro morreu, retorna 0.
    """
    direcao = determina_direcao(teclas)
    if direcao == "":
        return 2, None

    if not aventureiro.andar(direcao):
        return 2, None

    efeito = random.choices(["nada", "monstro"], [0.6, 0.4])[0]
    if efeito == "monstro":
        monstro = random.choices([Thanos, Demogorgon])[0](aventureiro.dificuldade)
        return int(iniciar_combate(aventureiro, monstro)), monstro.nome

    return 2, None

def jogo():
    """
    Fluxo principal do jogo, possui as seguintes etapas:
    - Inicia um aventureiro
    - Inicia um tesouro
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
                    resultado, nome_monstro = movimentar(aventureiro, teclas)
                    if resultado == 0:
                        mensagem_combate = f"Você foi derrotado por {nome_monstro}..."
                        jogo_acabou = True
                    elif resultado == 1:
                        mensagem_combate = f"{nome_monstro} foi derrotado!"
                    else:
                        mensagem_combate = "Você não encontrou nada"

                    if aventureiro.posicao == tesouro.posicao:
                        boss = Boss(aventureiro.dificuldade)
                        if iniciar_combate(aventureiro, boss):
                            mensagem_combate = f"Parabéns, {aventureiro.nome}, você encontrou o tesouro!"
                        else:
                            mensagem_combate = f"Você foi derrotado pelo chefão... =("

                        jogo_acabou = True

        # Desenho na tela
        tela.renderizar(aventureiro, tesouro, mensagem_combate)

        # Chamar o relógio interno do jogo
        pygame.time.Clock().tick(60)
