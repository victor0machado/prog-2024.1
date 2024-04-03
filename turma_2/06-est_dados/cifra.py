"""
Programação Estruturada
2024.1
03/04/2024
"""
import random

def alfabeto():
    return [chr(i) for i in range(97, 123)]

def gera_chave():
    chave = {}
    letras = alfabeto()

    letras_cifradas = alfabeto()
    random.shuffle(letras_cifradas)

    for char, char_cifrado in zip(letras, letras_cifradas):
        chave[char] = char_cifrado

    return chave

def cripto(mensagem, chave):
    mensagem_cifrada = ""

    for char in mensagem:
        mensagem_cifrada += chave[char]

    return mensagem_cifrada

def decripto(mensagem, chave):
    chave_inversa = {}
    for ch, vl in chave.items():
        chave_inversa[vl] = ch

    return cripto(mensagem, chave_inversa)

def main():
    chave = gera_chave()

    while True:
        msg = input("Informe a mensagem: ")
        op = input("0 para sair, 1 para cifrar ou outro valor para decifrar: ")
        if op == "0":
            break
        if op == "1":
            print(cripto(msg, chave))
        else:
            print(decripto(msg, chave))

main()
