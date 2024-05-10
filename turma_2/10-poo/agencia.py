from conta import Conta

class Agencia:
    def __init__(self, numero, endereco, gerente):
        self.numero = numero
        self.endereco = endereco
        self.gerente = gerente
        self.contador_contas = 0

    def abrir_nova_conta(self, titular):
        self.contador_contas += 1
        if self.gerente.autorizar_abertura_conta(self.contador_contas):
            return Conta(self.contador_contas, titular)

        return None

    def __str__(self):
        return f"Agência número {self.numero} - {self.endereco}, gerente {self.gerente}"

    def __eq__(self, __value: object) -> bool:
        if __value.__class__ != self.__class__:
            return False

        return self.numero == __value.numero
