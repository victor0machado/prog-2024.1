from jogo.mecanicas import relogio
from jogo.mecanicas.loop import jogo

import pygame

def iniciar():
    pygame.init()
    relogio.iniciar_tempo()

def encerrar():
    print("Saindo do jogo!")
    pygame.quit()

def main():
    iniciar()
    jogo()
    encerrar()

if __name__ == "__main__":
    main()
