#!/usr/bin/python3
from time import sleep

x = 1
num = int(input('Digite um numero: '))
while x <= num:
    print(f'numero: {x}')
    x += 1
    sleep(1)