#!/usr/bin/python
# coding: utf-8
    
def entrada():
    n= -1
    while n<=0:
        n=int(input('Digite um numero positivo: '))
    return n

def conta_divisor(n):
    ndiv=0
    for cont in range(1, n+1):
        resto = n%cont
        if resto==0:
            ndiv=ndiv+1
    return ndiv
        
def main():
    n = entrada()
    print(conta_divisor(n))
    
main()