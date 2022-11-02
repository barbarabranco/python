#!/usr/bin/python
# coding: utf-8

def area_quadrada(lado):
    return lado ** 2

def entrada():
    lado = float(input('Lado: '))
    return lado

def main():
    l = entrada()
    a = area_quadrada(l)
    print('Area: %.2f' % a)
    
main()