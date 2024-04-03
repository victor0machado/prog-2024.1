def aventureiro_andar(aventureiro, direcao):
    """
    Altera o valor da posicao do aventureiro conforme a direção informada pelo
    usuário. Direções válidas:
    - W: cima
    - A: esquerda
    - S: baixo
    - D: direita

    Se o aventureiro estiver nos limites do mapa, não faz nenhum movimento.

    Considerar que o mapa é um sistema cartesiano, com o eixo x aumentando
    da esquerda para a direita, e o eixo y aumentando de cima para baixo.
    Portanto, as coordenadas (0, 0) estão no canto superior esquerdo do mapa,
    enquanto que as coordenadas (9, 9) estão no canto inferior direito.

    Retorna True caso o aventureiro tenha andado, e False caso contrário.
    """

aventureiro = {"posicao": [0, 0]}

aventureiro_andar(aventureiro, "d")
print(aventureiro["posicao"]) # [1, 0]

aventureiro_andar(aventureiro, "w")
print(aventureiro["posicao"]) # [1, 0]

aventureiro_andar(aventureiro, "s")
print(aventureiro["posicao"]) # [1, 1]

aventureiro_andar(aventureiro, "a")
print(aventureiro["posicao"]) # [0, 1]

aventureiro_andar(aventureiro, "a")
print(aventureiro["posicao"]) # [0, 1]

aventureiro = {"posicao": [9, 9]}

aventureiro_andar(aventureiro, "d")
print(aventureiro["posicao"]) # [9, 9]

aventureiro_andar(aventureiro, "w")
print(aventureiro["posicao"]) # [9, 8]

aventureiro_andar(aventureiro, "s")
print(aventureiro["posicao"]) # [9, 9]

aventureiro_andar(aventureiro, "s")
print(aventureiro["posicao"]) # [9, 9]

def aventureiro_atacar(aventureiro):
    """
    Retorna um inteiro igual à Força do aventureiro, mais um valor aleatório
    entre 1 e 6.
    """

aventureiro = {"ataque": 5}
print(aventureiro_atacar(aventureiro))
print(aventureiro_atacar(aventureiro))
print(aventureiro_atacar(aventureiro))
print(aventureiro_atacar(aventureiro))
print(aventureiro_atacar(aventureiro))

