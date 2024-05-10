from jogo.mecanicas import jogo

import pygame

def iniciar():
    pygame.init()

def encerrar():
    print("Saindo do jogo!")
    pygame.quit()

def main():
    iniciar()
    jogo()
    encerrar()

if __name__ == "__main__":
    main()
