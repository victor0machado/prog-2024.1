class Agencia:
    def __init__(self, numero, endereco):
        self.numero = numero
        self.endereco = endereco
        self.contador_contas = 0

    def definir_nova_conta(self):
        self.contador_contas += 1
        return self.contador_contas

    def __str__(self):
        return f"Agência {self.numero}: {self.endereco}"

    def __eq__(self, __value: object) -> bool:
        if __value.__class__ != self.__class__:
            return False

        return self.numero == __value.numero
