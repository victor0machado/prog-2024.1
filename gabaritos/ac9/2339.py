comp, qtd, qtd_pessoa = [int(i) for i in input().split()]
if qtd_pessoa * comp > qtd:
    print("N")
else:
    print("S")
