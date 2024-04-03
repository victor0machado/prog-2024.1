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
