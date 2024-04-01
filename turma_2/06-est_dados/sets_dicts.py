"""
Programação Estruturada
2024.1
01/04/2024

Conjuntos
- Imutáveis
- Desordenados
- Únicos
- Não consigo acessar diretamente um elemento

Dicionários
- Imutáveis
- Desordenados
- Únicos
- Consigo acessar diretamente um elemento, a partir de sua chave
"""

def sets_dicts():
    conj = {"uva", "morango", "banana", "uva", "uva"}
    print(conj)
    for fruta in conj:
        print(fruta)

    print("pêssego" in conj)
    # print(conj[2]) -> TypeError

    lista = [2, 4, 5, 3, 2, 3, 1, 7, 5, 3]
    lista = list(set(lista))
    print(lista)

    alunos = ["zé", "ana", "álvaro"]
    notas = [7.5, 8.2, 3.4]
    cursos = ["EC", "ES", "CD"]

    alunos.sort()
    print(alunos, notas)

    # { chave: valor }
    alunos = {
        "zé": [7.5, "EC"],
        "ana": [8.2, "ES"],
        "álvaro": [3.4, "CD"]
    }
    alunos["maria"] = [6.7, "ES"]
    alunos["ana"] = [8.3, "ES"]
    print(alunos)
    print(alunos["ana"])

    # print(alunos["victor"]) -> KeyError

    # Método `get` retorna None caso a chave não exista
    print(alunos.get("victor"))
    print(alunos.get("victor", "Erro! Nome não encontrado."))

    print("-" * 30)

    alunos = [
        {
            "nome": "ana",
            "nota": 8.3,
            "curso": "ES",
            "disciplinas": ["Programação", "Cálculo"]
        },
        {
            "nome": "zé",
            "nota": 7.5,
            "curso": "EC"
        },
        {
            "nome": "álvaro",
            "nota": 3.4,
            "curso": "CD"
        }
    ]

    print("-" * 30)
    for aluno in alunos:
        for chave, valor in aluno.items():
            print(chave, valor)
    print("-" * 30)

    print(alunos[0]["nome"])
    print(alunos[0]["nota"])
    print(alunos[0]["curso"])

    aluno = {
        "nome": "ana",
        "nota": 7.3,
        "curso": "ES"
    }

    print("-" * 30)
    for chave in aluno.keys():
        print(chave)

    for valor in aluno.values():
        print(valor)

    for chave, valor in aluno.items():
        print(chave, valor)

def op1():
    print("Opção 1 selecionada")

def op2():
    print("Opção 2 selecionada")

def op3():
    print("Opção 3 selecionada")

def erro():
    print("Opção inválida!")

opcoes = {
    "1": op1,
    "2": op2,
    "3": op3
}

def main():
    while True:
        print("1 - Opção 1")
        print("2 - Opção 2")
        print("3 - Opção 3")
        opcao = input("Informe a opção desejada: ")
        opcoes.get(opcao, erro)()

main()
