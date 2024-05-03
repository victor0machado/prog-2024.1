# CamelCase
class Conta:
    # Método construtor
    def __init__(self, agencia):
        self.agencia = agencia
        self.numero = self.agencia.abrir_conta()
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def ver_saldo(self):
        return self.saldo

    # sobrescrita de métodos
    def __str__(self):
        return f"conta {self.numero}, {self.agencia} - saldo R$ {self.saldo:.2f}"

    def __eq__(self, __value: object) -> bool:
        if __value.__class__ != self.__class__:
            return False

        return self.agencia == __value.agencia and self.numero == __value.numero
