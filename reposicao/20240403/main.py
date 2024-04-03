import lista

def main():
    texto = 'olá, mundo'
    texto = "olá, mundo"
    
    dic = {
        "nome": 'victor'
    }
    
    print(dic['nome'])
    print(dic["nome"])

print(__name__)
if __name__ == "__main__":
    main()

x = 2
y = 10

if x >= 0:
    print("a")
elif y > 0:
    print("b")
elif x == 2 and y == 10:
    print("c")
else:
    print("d")

x = 2
print(f"O número é {x:6.2f}.")
print("O número é {:6.2f}.".format(x))
print("O número é %d." % x)
