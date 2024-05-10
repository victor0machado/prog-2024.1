# CamelCase
class Conta:
    def __init__(self, titular, agencia):
        self.titular = titular
        self.agencia = agencia
        self.numero = agencia.definir_nova_conta()
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        # self.saldo = self.saldo + valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def ver_saldo(self):
        return self.saldo

    # sobrescrita de método
    def __str__(self) -> str:
        return f"Conta de {self.titular}, número {self.numero} - saldo R$ {self.saldo:.2f}"

    def __eq__(self, __value: object) -> bool:
        if __value.__class__ != self.__class__:
            return False

        return self.numero == __value.numero and self.titular == __value.titular
