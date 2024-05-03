class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def trocar_email(self, novo_email):
        self.email = novo_email
