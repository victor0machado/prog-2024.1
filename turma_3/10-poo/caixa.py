from funcionario import Funcionario

class Caixa(Funcionario):
    def __init__(self, nome, matricula, email, agencia):
        super().__init__(nome, matricula, email, agencia)
        self.horario = ""

    def definir_horario_atendimento(self, novo_horario):
        self.horario = novo_horario
