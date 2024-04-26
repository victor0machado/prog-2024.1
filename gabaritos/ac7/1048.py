salario = float(input())

if salario <= 400:
    perc = 0.15
elif salario <= 800:
    perc = 0.12
elif salario <= 1200:
    perc = 0.1
elif salario <= 2000:
    perc = 0.07
else:
    perc = 0.04

aumento = round(perc * salario, 2)
print(f"Novo salario: {(salario + aumento):.2f}")
print(f"Reajuste ganho: {aumento:.2f}")
print(f"Em percentual: {perc * 100:.0f} %")
