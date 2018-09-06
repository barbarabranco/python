#!/usr/bin/python3
from time import sleep

matriz = [
    [1, 3, 6],
    [3, 5, 7],
    [6, 9, 11]
]

a = 0
b = 0
#enumera e cada elemento de uma lista (ex: 0, 1, 2 ...)
for cont, x in enumerate(matriz):
    a += x[cont]
    b += x[-(cont+1)]
print(a + b)
sleep(5)