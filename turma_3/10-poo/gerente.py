from conta import Conta
from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, matricula, email, agencia):
        super().__init__(nome, matricula, email, agencia)

    def abrir_nova_conta(self, titular):
        return Conta(titular, self.agencia)
