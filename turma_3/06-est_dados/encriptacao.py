"""
Programação Estruturada
2024.1
02/04/2024

Aplicação prática: Encriptando mensagens
"""
import random

def alfabeto():
    return [chr(unicode) for unicode in range(97, 123)]

def gera_chave():
    alfa = alfabeto()
    random.shuffle(alfa)

    chave = {}
    for letra, letra_embaralhada in zip(alfabeto(), alfa):
        chave[letra] = letra_embaralhada

    return chave

def cripto(mensagem, chave):
    mensagem_cifrada = ""
    for caractere in mensagem:
        # mensagem_cifrada = mensagem_cifrada + chave[caractere]
        mensagem_cifrada += chave[caractere]

    return mensagem_cifrada

def decripto(mensagem, chave):
    chave_inversa = {valor: ch for ch, valor in chave.items()}
    return cripto(mensagem, chave_inversa)

def main():
    chave = gera_chave()

    while True:
        mensagem = input("Digite a mensagem, ou ENTER para sair: ")
        if mensagem == "":
            break

        opcao = int(input("Informe 1 para encriptar ou outro valor para decriptar a mensagem: "))
        if opcao == 1:
            print(cripto(mensagem, chave))
        else:
            print(decripto(mensagem, chave))

main()
