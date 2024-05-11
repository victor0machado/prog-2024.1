import random

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
        print(f"{aventureiro.nome} causa {dano} de dano! Vida do monstro: {monstro.vida}")
        if not monstro.esta_vivo():
            print("Monstro foi derrotado!")
            aventureiro.ganhar_xp(monstro.xp)
            return True

        dano = monstro.atacar()
        aventureiro.defender(dano)
        print(f"Monstro causa {dano} de dano! Vida de {aventureiro.nome}: {aventureiro.vida}")
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

    if not aventureiro.andar(direcao):
        return 2

    efeito = random.choices(["nada", "monstro"], [0.6, 0.4])[0]
    if efeito == "monstro":
        monstro = Monstro()
        return int(iniciar_combate(aventureiro, monstro))

    return 2
