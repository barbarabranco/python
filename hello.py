#!/usr/bin/python
# coding: utf-8
from time import sleep
mensagem = "Hello World!!!"
print(mensagem)
nome = input("Qual o melhor curso de programação: ")
if nome == "python":
	print("Você acertou!!!")
	sleep(5)
else:
	print("Errou! =( ")
	sleep(5)