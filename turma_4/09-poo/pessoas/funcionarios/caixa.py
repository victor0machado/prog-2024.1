from .funcionario import Funcionario

class Caixa(Funcionario):
    def __init__(self, nome, matricula, email):
        super().__init__(nome, matricula, email)
        self.guiche = 0

    def atribuir_guiche(self, guiche):
        self.guiche = guiche
