import time

from jogo.mecanicas import som
from jogo.mecanicas import loop
from jogo.gui.relogio import relogio

import pygame

def iniciar():
    pygame.init()
    pygame.mixer.init()
    som.reproduzir_musica()
    relogio.iniciar()

def encerrar():
    print("Saindo do jogo!")
    pygame.quit()

def main():
    iniciar()
    loop.executar()
    time.sleep(2)
    encerrar()

if __name__ == "__main__":
    main()
