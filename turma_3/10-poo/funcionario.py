from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, matricula, email, agencia):
        super().__init__(nome, email)
        self.matricula = matricula
        self.agencia = agencia

    def trocar_email(self, novo_email):
        self.email = novo_email
