import random

XP_POR_NIVEL = 5

class Aventureiro:
    def __init__(self):
        self.forca = random.randint(10, 18)
        self.defesa = random.randint(10, 18)
        self.vida_max = random.randint(100, 120)
        self.vida = self.vida_max
        self.posicao = [0, 0]
        # self.nome = input("Deseja buscar um tesouro? Primeiro, informe seu nome: ")
        self.nome = "Qualquer coisa"
        self.nivel = 1
        self.xp = 0

    def ganhar_xp(self, xp_ganha):
        self.xp += xp_ganha
        if self.xp >= XP_POR_NIVEL * self.nivel:
            self.xp -= XP_POR_NIVEL * self.nivel
            self.ganhar_nivel()

    def ganhar_nivel(self):
        self.nivel += 1
        self.vida_max += 10
        self.vida = self.vida_max
        self.forca += 2
        self.defesa += 2
        print(f"{self.nome} ganhou um nível!")

    def calcular_pos_futura(self, direcao):
        x, y = self.posicao
        match direcao:
            case "A":
                x -= 1
            case "W":
                y -= 1
            case "S":
                y += 1
            case "D":
                x += 1

        return [x, y]

    def andar(self, pos_futura):
        self.posicao = pos_futura

    def atacar(self):
        """
        Retorna um inteiro igual à Força do aventureiro, mais um valor aleatório
        entre 1 e 6.
        """
        return self.forca + random.randint(1, 6)

    def defender(self, dano):
        """
        Calcula o dano a ser absorvido pelo aventureiro, igual ao dano causado
        menos o atributo de defesa do aventureiro.

        Se o dano a ser absorvido é menor ou igual a zero, não faz nada. Se for
        maior que zero, reduz esse dano da vida do aventureiro.
        """
        dano_levado = dano - self.defesa
        if dano_levado > 0:
            self.vida -= dano_levado

    def esta_vivo(self):
        """
        Retorna True se a vida do aventureiro é maior que zero.
        """
        return self.vida > 0

    def __str__(self):
        return f"""Aventureiro {self.nome}:
Força:  {self.forca}
Defesa: {self.defesa}
Vida:   {self.vida}
"""
