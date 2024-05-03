from ..pessoa import Pessoa

class Titular(Pessoa):
    def __init__(self, nome, email, conta):
        super().__init__(nome, email)
        self.conta = conta
