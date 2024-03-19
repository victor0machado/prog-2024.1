"""
Programação Estruturada
2024.1

AC2
Gabarito
"""

# Exercício 1
def eq_seg_grau(a, b, c):
    delta = b ** 2 - 4 * a * c
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    return x1, x2

def bissexto(ano):
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

# Exercício 2
def calcula_salario(valor_hora, num_horas, irpf=0.275):
    return valor_hora * num_horas * (1 - irpf)
