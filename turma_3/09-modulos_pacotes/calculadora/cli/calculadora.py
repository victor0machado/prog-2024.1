from ..numeros import decisor

def iniciar():
    n1 = float(input("Informe um valor: "))
    oper = input("Informe a operação (+, -, *, /): ")
    n2 = float(input("Informe outro valor: "))

    print(decisor.executar(n1, n2, oper))
