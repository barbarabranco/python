#!/usr/bin/python
# coding: utf-8

def soma(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mult(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

def menu():
  print(' 1 - Soma \n 2 - Subtracao \n 3 - Multiplicacao \n 4 - Divisao \n 5 - Sair')
  op = int(input('Escolha uma opcao: '))
  while(op<1 or op>5):
    print('Opcao invalida!')
    op = int(input('Escolha uma opcao: '))
  return op

def entrada():
  return int(input())

def escolha(op, n1, n2):
  if op == 1:
    result = soma(n1,n2)
  elif op == 2:
    result = sub(n1,n2)
  elif op == 3:
    result = mult(n1,n2)
  elif op == 4:
    if n2 != 0:
      result = div(n1,n2)
    else:
      result = None
  return result

def main():
  while True:
    op = menu()
    if op == 5:
      break
    print('Digite dois(2) numeros: ')
    n1 = entrada()
    n2 = entrada()
    if escolha(op, n1, n2) == None:
      print('Não há divisão por zero!')
    else:
      print(escolha(op,n1,n2))

main()