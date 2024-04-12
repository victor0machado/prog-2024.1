def func1(n):
    print(1 / n)

def func2():
    func1(0)

def func3():
    func2()

def main():
    func3()

main()
