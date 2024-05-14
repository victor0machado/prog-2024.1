from .inimigo import Inimigo

class Monstro(Inimigo):
    def __init__(self):
        super().__init__()
        print("Um novo monstro apareceu!")
