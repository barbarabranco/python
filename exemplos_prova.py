par = []
#numeros = [12, 45, 24, 67, 86, 43, 27]
numeros=[]
  while numeros<10:
    numeros.append(input("Digite um numero"))
    numeros+=1
for x in range(numeros):
    if x % 2 == 0:
        par.append(x)
print(par)
