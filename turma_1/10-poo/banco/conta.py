from datetime import datetime

class Conta:
    def __init__(self, agencia):
        self.agencia = agencia
        self.numero = self.agencia.criar_numero_conta()

        self.data_inicio = datetime.today()
        self.saldo = 0

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor

    def verificar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor
