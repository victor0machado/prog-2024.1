ent1 = input()
ent2 = input()

dados1 = ent1.split(" ")
dados2 = ent2.split(" ")

a_pagar = int(dados1[1]) * float(dados1[2]) + int(dados2[1]) * float(dados2[2])

print(f"VALOR A PAGAR: R$ {a_pagar:.2f}")