nome = input('Digite o seu nome: ')
separa = nome.split()

print(nome.upper())
print(nome.lower())
print('Seu nome completo tem {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))