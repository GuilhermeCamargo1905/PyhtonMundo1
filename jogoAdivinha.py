from random import randint

numero = int(input('Digite um número de 0 a 5: '))

escolhido = randint(0,5)

if numero == escolhido:
    print('Você acertou')
else:
    print('Você errou')
