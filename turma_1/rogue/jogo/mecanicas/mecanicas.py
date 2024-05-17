import random

from .armadilha import Armadilha

from jogo.personagens.monstro import Monstro

import pygame

def iniciar_combate(aventureiro, monstro):
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
        monstro.defender(dano)
        if not monstro.esta_vivo():
            aventureiro.status = "Monstro foi derrotado!"
            aventureiro.ganhar_xp(monstro.xp)
            return True

        dano = monstro.atacar()
        aventureiro.defender(dano)
        if not aventureiro.esta_vivo():
            aventureiro.status = f"{aventureiro.nome} foi derrotado!"
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

def movimentar(aventureiro, teclas, obstaculos):
    """
    Realiza a ação de movimento e analisa as consequências.

    Chama a o método andar do objeto aventureiro e analisa o seu resultado.

    Em seguida, analisa o efeito do movimento. Há 60% de chance de nada
    acontecer, e 40% de chance de um monstro aparecer (pesquise sobre a função
    random.choices).

    Se um monstro aparecer, inicia um novo monstro e retorna e resultado da
    função iniciar_combate.

    Retorna 0 se o aventureiro morreu.
    Retorna 1 se o aventureiro venceu um combate.
    Retorna 2 se nada aconteceu.
    """
    direcao = determina_direcao(teclas)
    if direcao == "":
        return 2

    pos_futura = aventureiro.calcular_pos_futura(direcao)
    if obstaculos.verificar_posicao(pos_futura):
        aventureiro.andar(pos_futura)
    else:
        return 2

    evento = random.choices(["armadilha", "nada", "monstro"], [0.2, 0.4, 0.4])[0]
    if evento == "armadilha":
        Armadilha().aplicar_efeito(aventureiro)
        if not aventureiro.esta_vivo():
            return 0
    elif evento == "monstro":
        monstro = Monstro()
        return int(iniciar_combate(aventureiro, monstro))

    return 2
