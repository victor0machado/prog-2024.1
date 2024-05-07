from caixa import Caixa
from agencia import Agencia
from gerente import Gerente

ag1 = Agencia(1, "Barra")

gerente = Gerente("João", 12, "joao@banco.com", ag1)

c1 = gerente.abrir_nova_conta("zé")
c2 = gerente.abrir_nova_conta("maria")

print(c1.saldo)
print(c1.titular)
print(c2.titular)

c1.depositar(50)
print(c1.ver_saldo())

c2.depositar(10)
print(c2.ver_saldo())

print(c1)
print(c2)

c3 = gerente.abrir_nova_conta("zé")
c3.depositar(50)

print(c1 == c3)

print("------------")

caixa1 = Caixa("marcelo", 17, "marcelo@banco.com", ag1)
caixa1.trocar_email("m@banco.com")

print(caixa1.email)
