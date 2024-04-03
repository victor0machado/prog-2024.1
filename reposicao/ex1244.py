def ex1244_sol1():
    n = int(input())
    for _ in range(n):
        entrada = input()
        palavras = entrada.split(" ")
        
        palavras.sort(key=len, reverse=True)
        print(" ".join(palavras))

def ex1244_sol2():
    entrada = input()
    palavras = entrada.split(" ")
    
    comprimentos = [len(palavra) for palavra in palavras]
    comprimentos.sort(reverse=True)
    
    palavras_ordenadas = []
    for comp in comprimentos:
        for palavra in palavras:
            if comp == len(palavra):
                palavras_ordenadas.append(palavra)
                palavras.remove(palavra)
                break
    
    print(palavras_ordenadas)


