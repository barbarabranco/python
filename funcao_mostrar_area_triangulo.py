#!/usr/bin/python
# coding: utf-8

def area_triangulo(base,altura):
    area = (base * altura) / 2
    return area

def entrada():
    valor = float(input('Valor: '))
    return valor

def main():
    base = float(input('base: '))
    altura = float(input('altura: '))
    area = area_triangulo(base, altura)
    print('Area: %.2f' % area)
    
main()