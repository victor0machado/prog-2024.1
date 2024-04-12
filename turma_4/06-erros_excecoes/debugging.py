def func1(n):
    print(11)

def func2(x):
    # x = int(input("informe um número: "))
    func1(10)

def func3():
    nomes = input("Informe os nomes, separados por espaço: ")
    nomes = nomes.split(" ")
    func2(nomes)

def main():
    func3()

main()
