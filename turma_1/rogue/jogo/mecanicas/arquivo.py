import os
import json
import os.path

from ..gui.relogio import relogio

from ..personagens.aventureiro.aventureiro import Aventureiro
from ..personagens.aventureiro.guerreiro import Guerreiro
from ..personagens.aventureiro.tank import Tank
from ..personagens.obstaculo import Obstaculos
from ..personagens.tesouro import Tesouro

CAMINHO = os.path.join(os.getcwd(), "out", "save.json")

def salvar(aventureiros, tesouro, obstaculos):
    dados = {
        "aventureiros": [aventureiro.exportar() for aventureiro in aventureiros],
        "tesouro": tesouro.exportar(),
        "obstaculos": obstaculos.exportar(),
        "relogio": relogio.exportar()
    }
    with open(CAMINHO, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

def existe():
    return os.path.isfile(CAMINHO)

def abrir():
    with open(CAMINHO, "r") as arquivo:
        dados = json.load(arquivo)

    relogio.importar(dados["relogio"])

    tesouro = Tesouro()
    tesouro.importar(dados["tesouro"])

    obstaculos = Obstaculos(len(dados["obstaculos"]), tesouro)
    obstaculos.importar(dados["obstaculos"])

    aventureiros = [None, None]

    for i, av in enumerate(dados["aventureiros"]):
        nome = av["nome"]
        classe = av["classe"]
        match classe:
            case "Aventureiro":
                aventureiro = Aventureiro(nome, i)
            case "Guerreiro":
                aventureiro = Guerreiro(nome, i)
            case "Tank":
                aventureiro = Tank(nome, i)

        aventureiro.importar(av)
        aventureiros[i] = aventureiro

    return aventureiros, tesouro, obstaculos
