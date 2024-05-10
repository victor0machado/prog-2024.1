import random

from jogo.gui.tela import Tela

from jogo.personagens.monstro import Monstro
from jogo.personagens.aventureiro import Aventureiro
from jogo.personagens.tesouro import Tesouro

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
        return 2

    if not aventureiro.andar(direcao):
        return 2

    efeito = random.choices(["nada", "monstro"], [0.6, 0.4])[0]
    if efeito == "monstro":
        monstro = Monstro()
        return int(iniciar_combate(aventureiro, monstro))

    return 2

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
    while True:
        # Controlar os eventos
        teclas = pygame.key.get_pressed()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

            if evento.type == pygame.KEYUP:
                if teclas[pygame.K_q]:
                    print("Já correndo?")
                    return

                # Executar as ações do jogo
                resultado = movimentar(aventureiro, teclas)
                if resultado == 0:
                    return

                if resultado == 1:
                    mensagem_combate = "Monstro foi derrotado!"
                else:
                    mensagem_combate = ""

                if aventureiro.posicao == tesouro.posicao:
                    print(f"Parabéns, {aventureiro.nome}, você encontrou o tesouro!")
                    return

        # Desenho na tela
        tela.renderizar(aventureiro, tesouro, mensagem_combate)

        # Chamar o relógio interno do jogo
        pygame.time.Clock().tick(60)
