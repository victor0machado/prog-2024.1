"""
Programação Estruturada
2024.1
02/04/2024

Aplicação prática: Cifra de César
"""
def determina_letra(cod_unicode):
    return (cod_unicode - 97) % 26 + 97

def cripto(mensagem, chave):
    mensagem_encriptada = ""

    for caractere in mensagem:
        caractere_encriptado = chr(determina_letra(ord(caractere) + chave))
        mensagem_encriptada += caractere_encriptado

    return mensagem_encriptada

def decripto(mensagem, chave):
    return cripto(mensagem, -1 * chave)

print(cripto("faca", 2)) # rkbbc
print(cripto("pizza", 2)) # rkbbc
print(cripto("pizza", 5)) # uneef

print(decripto("uneef", 5))
