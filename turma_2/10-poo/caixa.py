from funcionario import Funcionario

class Caixa(Funcionario):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email, matricula)
        self.guiche = 0

    def atribuir_guiche(self, novo_guiche):
        self.guiche = novo_guiche
