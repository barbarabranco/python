#!/usr/bin/python3
from time import sleep

par = []
numeros = [12, 45, 24, 67, 86, 43, 27]
for x in numeros:
    if x % 2 == 0:
        par.append(x)
print(par)
sleep(3)
