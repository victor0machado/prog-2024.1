import time

from jogo.mecanicas import loop

import pygame

def iniciar():
    pygame.init()

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
