from .pessoa import Pessoa

class Titular(Pessoa):
    def __init__(self, nome, email, conta):
        super().__init__(nome, email)
        self.conta = conta

    def __str__(self):
        return f"{self.nome}, {self.email} - saldo R$ {self.conta.verificar_saldo():.2f}"
