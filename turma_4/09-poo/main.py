from conta import Conta
from agencia import Agencia

ag1 = Agencia(1, "Barra", "Zé")
ag2 = Agencia(2, "Recreio", "Maria")

c1 = Conta(ag1)
c2 = Conta(ag2)

print(c1)
print(c2)

c1.depositar(50)
print(c1.ver_saldo())
print(c2.ver_saldo())

c3 = Conta(ag2)
print(c3)

print(c2 == c3)

c2.depositar(10)
print(c2.ver_saldo())
print(c3.ver_saldo())
print(c2 == c3)
