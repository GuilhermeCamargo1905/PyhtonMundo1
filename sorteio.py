from random import choice

n1 = input('Digite o número do 1 aluno: ')
n2 = input('Digite o número do 2 aluno: ')
n3 = input('Digite o número do 3 aluno: ')
n4 = input('Digite o número do 4 aluno: ')

lista = [n1, n2, n3, n4]

escolhido = choice(lista)

print(' ')
print('O aluno escolhido foi {}'.format(escolhido))