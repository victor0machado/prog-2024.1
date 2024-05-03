class Agencia:
    def __init__(self, numero, endereco, gerente):
        self.numero = numero
        self.endereco = endereco
        self.gerente = gerente
        self.contador_contas = 0

    def abrir_conta(self):
        self.contador_contas += 1
        return str(self.contador_contas).rjust(4, "0")

    def __str__(self):
        return f"agência {self.numero}, {self.endereco} - gerente: {self.gerente}"

    def __eq__(self, __value: object) -> bool:
        if __value.__class__ != self.__class__:
            return False

        return self.numero == __value.numero and self.endereco == __value.endereco
