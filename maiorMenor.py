n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 > n2 and n1 > n3:
    print('Maior é {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('Maior é {}'.format(n2))
else:
    print('Maior é {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor é {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor é {}'.format(n2))
else:
    print('menor é {}'.format(n3))
