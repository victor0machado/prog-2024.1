"""
Programação Estruturada
2024.1

AC4
Gabarito
"""

def ler_nome():
    """Retorna o nome do aluno inserido pelo usuário."""
    return input("Informe o seu nome: ")

def ler_notas():
    """Lê as notas de AP1, AP2, AS e AC do aluno, e retorna essas notas."""
    ap1 = float(input("Informe a nota da AP1: "))
    ap2 = float(input("Informe a nota da AP2: "))
    asub = float(input("Informe a nota da AS: "))
    ac = float(input("Informe a nota da AC: "))
    return ap1, ap2, asub, ac

def analisar_subst(ap1, ap2, asub):
    """
    Retorna as duas notas a serem usadas no cálculo.
    A AS deve substituir a AP1 ou AP2 se for maior que elas.
    """
    if ap1 <= ap2 and asub > ap1:
        return asub, ap2
    if ap2 <= ap1 and asub > ap2:
        return ap1, asub
    return ap1, ap2

def calcular_media(ap1, ap2, asub, ac):
    """Calcula e retorna a média final do aluno."""
    prova1, prova2 = analisar_subst(ap1, ap2, asub)
    return (prova1 + prova2) * 0.4 + ac * 0.2

def aluno_foi_aprovado(media):
    """Retorna True se a média foi suficiente para aprovação do aluno."""
    return media >= 7

def notas_sao_validas(ap1, ap2, asub, ac):
    """Retorna True se todas as notas estão entre 0 e 10, inclusive."""
    return 0 <= ap1 <= 10 and 0 <= ap2 <= 10 and 0 <= asub <= 10 and 0 <= ac <= 10

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            media = round(calcular_media(ap1, ap2, asub, ac), 2)
            print("Média final:", media)
            if aluno_foi_aprovado(media):
                print("Aluno foi aprovado.")
            else:
                print("Aluno foi reprovado.")

main()
