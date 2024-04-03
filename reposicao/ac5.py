import random

def main():
    aventureiro = {
        "vida": 100,
        "ataque": random.randint(10, 20),
        "defesa": random.randint(1, 5)
    }

    monstro = {
        "vida": random.randint(60, 80),
        "ataque": random.randint(20, 30)
    }

    print(
        "Aventureiro:",
        aventureiro["vida"],
        aventureiro["ataque"],
        aventureiro["defesa"]
    )
    print("Monstro:", monstro["vida"], monstro["ataque"])

    rodada = 1
    while True:
        print("Rodada", rodada)
        dano = random.randint(1, aventureiro["ataque"])
        monstro["vida"] -= dano
        if monstro["vida"] <= 0:
            print("Monstro morreu!")
            break

        dano = random.randint(1, monstro["ataque"]) - aventureiro["defesa"]
        if dano > 0:
            aventureiro["vida"] -= dano
            if aventureiro["vida"] <= 0:
                print("Você morreu!")
                break

        print(
            "Aventureiro:",
            aventureiro["vida"],
            aventureiro["ataque"],
            aventureiro["defesa"]
        )
        print("Monstro:", monstro["vida"], monstro["ataque"])
        rodada += 1

main()
