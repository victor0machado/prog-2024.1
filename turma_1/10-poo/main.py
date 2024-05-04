from banco import agencia
from banco.pessoas.gerente import Gerente

ag1 = agencia.Agencia(1, "Barra")
gerente = Gerente("Zé", "ze@banco.com", 1, ag1)

c1 = gerente.cadastrar_cliente("Ana", "ana@gmail.com")
print(c1)

c1.conta.depositar(100)
print(c1)

print(gerente.email)
gerente.trocar_email("ze@banco.com.br")
print(gerente.email)
