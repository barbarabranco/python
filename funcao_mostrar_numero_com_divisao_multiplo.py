#!/usr/bin/python
# coding: utf-8

def multiplo(n1,n2):
    if n1%n2==0:
        return True
    return False

def entrada():
    n = int(input('Digite um numero: '))
    return n

def main():
    x = entrada()
    y = entrada()
    print(multiplo(x,y))
    
main()