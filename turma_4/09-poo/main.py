from banco.agencia import Agencia
from pessoas.funcionarios.gerente import Gerente

ag1 = Agencia(1, "Barra")
gerente = Gerente("Zé", 1, "ze@banco.com", ag1)

cliente1 = gerente.cadastrar_novo_cliente("Ana", "ana@gmail.com")
print(cliente1.conta)
