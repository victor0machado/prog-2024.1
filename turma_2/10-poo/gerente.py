from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email, matricula)

    def autorizar_abertura_conta(self, numero):
        return numero <= 10
