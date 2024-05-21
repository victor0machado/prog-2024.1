import time
import random

from ..gui.tela import Tela

from ..personagens.aventureiro import Aventureiro
from ..personagens.monstros.monstro import Monstro
from ..personagens.monstros.chefe import Chefe
from ..personagens.tesouro import Tesouro

import pygame

def determinar_direcao(teclas):
    if teclas[pygame.K_a]:
        return "A"
    if teclas[pygame.K_w]:
        return "W"
    if teclas[pygame.K_s]:
        return "S"
    if teclas[pygame.K_d]:
        return "D"

    return ""

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
            return True

        dano = monstro.atacar()
        aventureiro.defender(dano)
        if not aventureiro.esta_vivo():
            return False

# Operação principal do jogo
def movimentar(aventureiro, direcao):
    """
    Realiza a ação de movimento e analisa as consequências.

    Chama a função aventureiro.andar e analisa o seu resultado. Se for False,
    ou seja, se o aventureiro não tiver andado nada, retorna True.

    Em seguida, analisa o efeito do movimento. Há 60% de chance de nada
    acontecer, e 40% de chance de um monstro aparecer (pesquise sobre a função
    random.choices).

    Se um monstro aparecer, inicia um novo monstro e retorna e resultado da
    função iniciar_combate.

    Caso não seja um monstro, retorna True.
    """
    if aventureiro.andar(direcao):
        efeito = random.choices(["nada", "monstro", "armadilha"], [0.5, 0.4, 0.1])[0]
        if efeito == "monstro":
            monstro = Monstro()
            if iniciar_combate(aventureiro, monstro):
                aventureiro.status = "Monstro foi derrotado!"
                return True

            return False
        if efeito == "armadilha":
            impacto = random.choices(["morte", "dano", "força", "defesa"], [0.05, 0.55, 0.2, 0.2])[0]
            match impacto:
                case "morte":
                    aventureiro.status = "Caiu numa armadilha! Morte instantânea..."
                    return False
                case "dano":
                    dano = random.randint(10, 25)
                    aventureiro.defender(dano, usar_defesa=False)
                    aventureiro.status = f"Caiu numa armadilha e sofreu {dano} de dano!"
                    if not aventureiro.esta_vivo():
                        return False
                case "força":
                    aventureiro.status = "Caiu numa armadilha e perdeu 1 de força!"
                    aventureiro.forca -= 1
                case "defesa":
                    aventureiro.status = "Caiu numa armadilha e perdeu 1 de defesa!"
                    aventureiro.defesa -= 1

            return True

    aventureiro.status = "Continue explorando"
    return True


def loop():
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

    jogo_rodando = True
    while jogo_rodando:
        # Mapeamento de eventos
        teclas = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

            if evento.type == pygame.KEYUP:
                # Processamento das ações
                if teclas[pygame.K_t]:
                    print(aventureiro)
                if teclas[pygame.K_q]:
                    aventureiro.status = "Já correndo?"
                    jogo_rodando = False

                if teclas[pygame.K_c]:
                    aventureiro.trocar_char()
                if teclas[pygame.K_v]:
                    aventureiro.trocar_cor()

                if not movimentar(aventureiro, determinar_direcao(teclas)):
                    aventureiro.status = "Game over..."
                    jogo_rodando = False

        if aventureiro.posicao == tesouro.posicao:
            chefe = Chefe()
            if iniciar_combate(aventureiro, chefe):
                aventureiro.status = "Você lutou contra o chefe e recuperou o tesouro!"
            else:
                aventureiro.status = "Você foi derrotado pelo chefe do jogo!"
            jogo_rodando = False

        # Renderização da tela
        tela.renderizar(aventureiro, tesouro)
        pygame.time.Clock().tick(60)

    time.sleep(2)
