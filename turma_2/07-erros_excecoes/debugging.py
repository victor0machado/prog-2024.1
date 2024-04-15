def func1(x):
    print(x + 2)

def func2():
    func1('a')

def func3():
    func2()

def main():
    func3()

main()
