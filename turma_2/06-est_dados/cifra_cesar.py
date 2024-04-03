"""
Programação Estruturada
2024.1
03/04/2024
"""

def unicode(codigo):
    return (codigo - 97) % 26 + 97

"""
char = 'z'
k = 2

ord(char) + k = 124

124 - 97 = 27
27 % 26 = 1
1 + 97 = 98
"""


def cifra_cesar(mensagem, k):
    mensagem_cifrada = ""

    for caractere in mensagem:
        caractere_cifrado = chr(unicode(ord(caractere) + k))
        mensagem_cifrada += caractere_cifrado

    return mensagem_cifrada

# chr(121) -> y
# chr(98) -> b
# ord('a') -> 97
# ord('f') -> 102

print(cifra_cesar("olamundo", 4))
print(cifra_cesar("iaca", -2))
print(cifra_cesar("pizza", 3))
