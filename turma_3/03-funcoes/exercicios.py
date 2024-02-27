"""
Programação Estruturada
2024.1
27/02/2024

Exercícios
"""

def media(ap1, ap2, ac):
    return (ap1 + ap2) * 0.4 + ac * 0.2

def converte_f_para_c(temp_fahr):
    return (5 / 9) * (temp_fahr - 32)

def main():
    print(media(8, 7, 6.5))
    print(converte_f_para_c(212))

main()
