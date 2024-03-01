"""
Programação Estruturada
2024.1
01/03/2024

Exercícios
"""

"""
1.
Faça um programa que peça as três notas da disciplina (AP1, AP2 e AC) e mostre
a média. A média é calculada de acordo com a fórmula
M = (AP1 + AP2) * 0.4 + AC * 0.2.
"""
def media():
    ap1 = float(input("Informe a nota da AP1: "))
    ap2 = float(input("Informe a nota da AP2: "))
    ac = float(input("Informe a nota da AC: "))

    media = (ap1 + ap2) * 0.4 + ac * 0.2

    print("A média é", round(media, 2))

"""
2.
Faça um programa que receba as três notas da disciplina (AP1, AP2 e AC) e
retorne a média. A média é calculada de acordo com a fórmula
M = (AP1 + AP2) * 0.4 + AC * 0.2.
"""
def outra_media(ap1, ap2, ac):
    return (ap1 + ap2) * 0.4 + ac * 0.2

def main():
    media()
    print(outra_media(7.7, 6.5, 7.3))

main()
