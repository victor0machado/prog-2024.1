from .funcionario import Funcionario
from .titular import Titular
from ..conta import Conta

class Gerente(Funcionario):
    def __init__(self, nome, email, matricula, agencia):
        super().__init__(nome, email, matricula)
        self.agencia = agencia

    def cadastrar_cliente(self, nome, email):
        nova_conta = Conta(self.agencia)
        return Titular(nome, email, nova_conta)
