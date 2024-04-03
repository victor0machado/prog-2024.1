"""
Imutável
Desordenado
Indexação
"""

def dic1():
    # chave: valor
    alunos = {
        "1234": "João",
        "5678": "Ana",
        "9101": "Maria"
    }
    
    print(alunos["1234"])
    print(alunos.get(2))
    print(alunos.get(2, "Não encontrado"))
    
    alunos["1112"] = "Luiza"
    print(alunos)
    
    alunos["1234"] = "Marcelo"
    print(alunos)

def dic2():
    alunos = {
        "1234": {
            "nome": "João",
            "curso": "ES",
            "período": 3,
            "disciplinas": [
                "Programação",
                "Cálculo",
                "GA"
            ]
        },
        "5678": {
            "nome": "Ana",
            "curso": "ADS",
            "período": 1,
            "disciplinas": [
                "Programação",
                "Web",
                "Design"
            ]
        }
    }
    
    # Percorrendo as chaves do dicionário
    for matricula in alunos:
        print(matricula)
    
    for matricula in alunos.keys():
        print(matricula)
    
    # Percorrendo os valores do dicionário
    for aluno in alunos.values():
        print(aluno)
    
    # Percorrendo chaves e valores do dicionário
    for matricula, aluno in alunos.items():
        print(matricula, aluno, sep=" - ")
    
def op1():
    print("Operação 1")

def op2():
    print("Operação 2")

def op3():
    print("Operação 3")

def erro():
    print("Erro! Opção não encontrada.")

operacoes = {
    "1": op1,
    "2": op2,
    "3": op3,
    "0": exit
}

while True:
    op = input("Informe a opção desejada: ")
    operacoes.get(op, erro)()
