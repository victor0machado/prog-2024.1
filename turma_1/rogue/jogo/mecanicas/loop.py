from .mecanicas import movimentar
from .mecanicas import iniciar_combate

from ..personagens.aventureiro.aventureiro import Aventureiro
from ..personagens.aventureiro.guerreiro import Guerreiro
from ..personagens.aventureiro.tank import Tank
from ..personagens.inimigos.chefe import Chefe
from ..personagens.tesouro import Tesouro
from ..personagens.obstaculo import Obstaculos
from ..gui.tela import Tela
from ..gui.input_texto import InputBox
from ..gui.menu_classe import MenuClasse

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

def selecionar_classe():
    menu = MenuClasse("Agora escolha sua classe:")

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "Aventureiro"

            if evento.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clique = MenuClasse.selecionou_botao(pos)
                if clique:
                    return clique

        menu.renderizar()

def executar():
    tesouro = Tesouro()
    obstaculos = Obstaculos(TOTAL_OBSTACULOS, tesouro)

    nome = input_box()
    classe = selecionar_classe()
    match classe:
        case "Aventureiro":
            aventureiro = Aventureiro()
        case "Guerreiro":
            aventureiro = Guerreiro()
        case "Tank":
            aventureiro = Tank()

    aventureiro.nome = nome

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
                else:
                    aventureiro.causar_dano_veneno()
                    if not aventureiro.esta_vivo():
                        aventureiro.status = "Você foi morto por veneno..."
                        aventureiro.fim_jogo = False
                        jogo_encerrou = True
                    elif aventureiro.posicao == tesouro.posicao:
                        chefe = Chefe()
                        if iniciar_combate(aventureiro, chefe):
                            aventureiro.status = f"Parabéns! Você derrotou {chefe.nome} e encontrou o tesouro!"
                            aventureiro.fim_jogo = True
                        else:
                            aventureiro.status = f"Você foi derrotado pelo {chefe.nome}..."
                            aventureiro.fim_jogo=  False

                        jogo_encerrou = True

        tela.renderizar(aventureiro, tesouro, obstaculos.obstaculos)
        pygame.time.Clock().tick(60)
