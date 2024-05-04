from .pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.matricula = matricula
        self.horario = ""

    def registrar_horario(self, horario):
        self.horario = horario
