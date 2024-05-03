from ..pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, matricula, email):
        super().__init__(nome, email)
        self.matricula = matricula
        self.horario = ""

    def definir_horario(self, horario):
        self.horario = horario
