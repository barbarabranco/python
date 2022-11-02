#!/usr/bin/python
# coding: utf-8

def maximo(n1,n2):
    if n1 > n2:
        return n1
    return n2

def entrada():
    n = int(input('Digite um numero: '))
    return n

def main():
    x = entrada()
    y = entrada()
    print(maximo(x,y))
    
main()