from random import shuffle

n1 = int(input('Digite o numero do 1 grupo: '))
n2 = int(input('Digite o número do 2 grupo: '))
n3 = int(input('Digite o número do 3 grupo: '))
n4 = int(input('Digite o número do 4 grupo: '))

lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)