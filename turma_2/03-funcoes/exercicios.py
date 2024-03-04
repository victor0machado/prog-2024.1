"""
Programação Estruturada
2024.1
04/03/2024

Exercícios
"""

"""
Nota 05
Exercício resolvido 01
Faça uma função media(), que recebe os parâmetros posicionais
ap1, ap2 e ac, e retorne a média de avaliações, utilizando a
fórmula M = (AP1 + AP2) * 0.4 + AC * 0.2.
"""
def media(ap1, ap2, ac):
    return round((ap1 + ap2) * 0.4 + ac * 0.2, 2)

"""
Nota 06
Exercício resolvido 04
Monte um conversor de temperatura, que recebe uma temperatura
em graus Fahrenheit e devolva a temperatura em graus Celsius.
A fórmula para conversão é C / 5 = (F - 32) / 9.
"""
def fahr_para_celsius(temp_fahr):
    return (5 / 9) * (temp_fahr - 32)

def main():
    print(media(8, 7, 5))
    print(media(6, 6, 6))
    print(media(10, 0, 0))
    print(fahr_para_celsius(212))
    print(fahr_para_celsius(32))

main()


