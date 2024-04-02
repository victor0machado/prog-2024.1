"""
Programação Estruturada
2024.1

AC5
Gabarito
"""
import random

def main():
    avent_vida = 100
    avent_att = random.randint(10, 20)
    avent_def = random.randint(1, 5)

    monstro_vida = random.randint(60, 80)
    monstro_att = random.randint(20, 30)

    print("Aventureiro: vida", avent_vida, "- att", avent_att, "- def", avent_def)
    print("Monstro: vida", monstro_vida, "- att", monstro_att)

    rodada = 1

    while True:
        print("Rodada", rodada)
        monstro_vida -= random.randint(1, avent_att)
        if monstro_vida <= 0:
            print("O monstro morreu!")
            break

        dano_monstro = random.randint(1, monstro_att) - avent_def
        if dano_monstro > 0:
            avent_vida -= dano_monstro
        if avent_vida <= 0:
            print("Você morreu!")
            break

        print("Aventureiro: vida", avent_vida, "- att", avent_att, "- def", avent_def)
        print("Monstro: vida", monstro_vida, "- att", monstro_att)
        rodada += 1

main()
