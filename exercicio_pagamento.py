#!/usr/bin/python
# coding: utf-8
    
def valorPagamento(valor, dias):
    if dias<=0:
        return valor
    valorAtraso = valor+(valor*0.03)+((valor*0.001)*dias)
    return valorAtraso
       
def main():
    valor = float(input('Prestacao: '))
    dias = int(input('Dias atraso: '))
    print(valorPagamento(valor, dias))
    
    
main()