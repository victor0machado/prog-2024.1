class Agencia:
    """
    numero
    endereco
    gerente
    """
    def __init__(self, numero, endereco, gerente):
        self.numero = numero
        self.endereco = endereco
        self.gerente = gerente
        self.contador_contas = 0

    def criar_numero_conta(self):
        self.contador_contas += 1
        return self.contador_contas

    def __str__(self):
        return f"Agência {self.endereco} - número {self.numero}"

    def __eq__(self, __value: object) -> bool:
        if __value.__class__ != self.__class__:
            return False

        return self.numero == __value.numero and self.endereco == __value.endereco
