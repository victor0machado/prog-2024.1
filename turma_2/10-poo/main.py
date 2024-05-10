from agencia import Agencia
from gerente import Gerente

ger1 = Gerente("Zé", "ze@banco.com", "1234")
ag1 = Agencia(1, "Barra", ger1)

print(ger1)

c1 = ag1.abrir_nova_conta("ana")
c2 = ag1.abrir_nova_conta("joão")

print(c1)
print(c2)

ag2 = Agencia(2, "Centro", ger1)

c3 = ag2.abrir_nova_conta("antonio")
print(c3)
