#!/usr/bin/python3
from time import sleep

nome = input('Digite o nome do aluno: ')
notas = int(input('Digite o numero de notas: '))
soma = 0
for x in range(notas):
    nota = int(input(f'Digite n{x+1}: '))
    soma += nota
media = soma / notas

print(f'A media do aluno {nome} foi {media}')
sleep(4)
if media > 6 and media < 8:
    print(f'{nome} foi aprovado')
    sleep(3)
elif media >= 8:
    print(f'{nome} foi aprovado com louvor!')
    sleep(3)
else:
    print(f'{nome} foi reprovado')
    sleep(3)