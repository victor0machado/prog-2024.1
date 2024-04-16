def func1(n):
    print(2 / n)

def func2():
    func1(0)

def func3():
    print('olá, mundo')
    func2()

def main():
    func3()

main()
