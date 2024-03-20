"""
Programação Estruturada
2024.1
19/03/2024

Estruturas de Dados
Conjuntos
- Imutáveis
- Desordenados
- Únicos

Dicionários
- Imutáveis
- Desordenados
- Únicos
- É possível acessar os dados individualmente, a partir de chaves
"""

def sets_dicts():
    lista = ["a", "b", "c", "a"]
    print(lista)

    conjunto = {"a", "b", "c", "a"}
    print(conjunto)
    # print(conjunto[2]) -> TypeError

    print(len(conjunto))
    for elemento in conjunto:
        print(elemento)

    print("f" in conjunto)

    # Remover dados repetidos em uma lista
    lista_unica = list(set(lista))
    print(lista_unica)

    print("-" * 30)
    print(lista_unica[2])

    # Dicionários (mapas em outras linguagens)
    alunos = {
        # chave: valor
        "202401222222": "zé",
        "202402333333": "ana"
    }
    print(alunos["202401222222"])
    print(alunos["202402333333"])
    # print(alunos[555]) # KeyError

    alunos["202403444444"] = "bruno"
    print(alunos)

    alunos["202402333333"] = "andré"
    print(alunos)

    if 555 in alunos.keys():
        print(alunos[555])

    alunos = {
        "1111": {
            "nome": "zé",
            "curso": "engenharia de software",
            "idade": 19,
            "período": 1
        },
        "2222": {
            "nome": "ana",
            "curso": "ciência de dados",
            "idade": 20,
            "período": 3
        }
    }
    print(alunos)
    print(alunos["2222"]["curso"])
    print(alunos.get("3333", "Erro! Matrícula não encontrada"))
    print(alunos.get("1111", "Erro! Matrícula não encontrada"))

    print("2222" in alunos.keys())

    for chave in alunos.keys():
        print(chave)

    for valor in alunos.values():
        print(valor)

    for chave, valor in alunos.items():
        print(chave, "-", valor)

def abrir_usuario():
    print("Abrindo usuário")

def editar_usuario():
    print("Editando usuário")

def excluir_usuario():
    print("Excluir usuário")

def erro():
    print("Opção inválida!")

opcoes = {
    "1": abrir_usuario,
    "2": editar_usuario,
    "3": excluir_usuario
}

def cli():
    msg = """Informe a opção desejada:
1 - Abrir usuário;
2 - Editar usuário;
3 - Excluir usuário
"""
    op = input(msg)
    opcoes.get(op, erro)()

cli()
