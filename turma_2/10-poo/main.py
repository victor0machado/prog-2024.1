from conta import Conta

c1 = Conta(1234, "João")
c2 = Conta(1234, "João")

print(c1.titular)
print(c2.titular)

c1.depositar(50)

print(c1.saldo)
print(c2.saldo)

c1.sacar(20)
tenta_sacar = c2.sacar(20)

if tenta_sacar:
    print("Saque feito com sucesso!")
else:
    print("Saldo insuficiente")

print(c1.saldo)
print(c2.saldo)

c2.depositar(30)

print(c1)
print(c2)
print(c1 == c2)
