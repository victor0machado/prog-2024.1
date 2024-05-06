
# CamelCase para nomear classes
class Conta:
    # método construtor
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False

        self.saldo -= valor
        return True

    # sobrescrita de método
    def __str__(self):
        return f"Conta de {self.titular}, número {self.numero}, saldo: R${self.saldo:.2f}"

    def __eq__(self, __value: object) -> bool:
        if __value.__class__ != self.__class__:
            return False

        return self.numero == __value.numero and self.saldo == __value.saldo
