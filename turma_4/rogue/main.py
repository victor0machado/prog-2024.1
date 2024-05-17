import time

from jogo.mecanicas.loop import jogo

import pygame

def iniciar():
    pygame.init()

def encerrar():
    print("Saindo do jogo!")
    pygame.quit()

def main():
    iniciar()
    jogo()
    time.sleep(2)
    encerrar()

if __name__ == "__main__":
    main()
