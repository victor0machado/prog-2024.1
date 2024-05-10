class Funcionario:
    def __init__(self, nome, email, matricula):
        self.nome = nome
        self.email = email
        self.matricula = matricula

    def trocar_email(self, novo_email):
        self.email = novo_email

    def __str__(self):
        return self.nome
