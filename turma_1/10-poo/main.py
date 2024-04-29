from banco import agencia, conta

ag1 = agencia.Agencia(1, "Barra", "Zé")
ag2 = agencia.Agencia(1, "Barra", "Ana")

print(ag1 == ag2)

# print(ag1)
# print(ag2)

# c1 = conta.Conta(ag1)
# c2 = conta.Conta(ag1)

# print(c1.numero)
# print(c2.numero)

# c1.depositar(100)
# print(c1.saldo)
# print(c2.saldo)
