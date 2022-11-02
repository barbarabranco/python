#!/usr/bin/python
# coding: utf-8

def atualiza_preco(valor):
    novo_valor=valor+(valor*0.10)
    return novo_valor

def taxa(valor):
    nova_tax=(valor*0.025)
    return nova_tax

def entrada():
    return float(input())

def main():
    print('Digite o valor do produto atual: ')
    valor = entrada()
    while(valor<=0):
        print('Produto nao pode ser menor ou igual a zero!')
        print('Digite o valor do produto atual: ')
        valor = entrada()
    novo_valor = atualiza_preco(valor)
    nova_tax = taxa(novo_valor)
    print('%.2f' % novo_valor)
    print('%.2f' % nova_tax)
    
main()