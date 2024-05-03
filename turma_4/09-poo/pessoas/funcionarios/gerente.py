from banco.conta import Conta

from ..clientes.titular import Titular
from .funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, matricula, email, agencia):
        super().__init__(nome, matricula, email)
        self.agencia = agencia

    def cadastrar_novo_cliente(self, nome, email):
        nova_conta = Conta(self.agencia)
        novo_cliente = Titular(nome, email, nova_conta)
        return novo_cliente
