#!/usr/bin/python3
from time import sleep
ling = {"daniel":"python", "barbara":"java", "fellipe":"R"}
print("Lista do Dicionario: {}" .format(ling))
sleep(3)
print("Objeto daniel do dicionario: {}" .format(ling["daniel"]))
sleep(3)
ling['daniel'] = input("Trocar o objeto do daniel: ")
print("Trocando o Objeto daniel do dicionario: {}" .format(ling["daniel"]))
sleep(4)
nome = 'barbara'
print(f'{nome} branco')
sleep(3)
