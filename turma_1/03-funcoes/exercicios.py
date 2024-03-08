"""
Programação Estruturada
2024.1
08/03/2024

Funções - Exercícios
Nota de aula 05
"""

"""
Exercício resolvido 01
Faça uma função media(), que recebe os parâmetros posicionais
ap1, ap2 e ac, e retorne a média de avaliações, utilizando a
fórmula M = (AP1 + AP2) * 0.4 + AC * 0.2.
"""
def media(ap1, ap2, ac):
    return (ap1 + ap2) * 0.4 + ac * 0.2

print(round(media(8, 5, 2), 1))
