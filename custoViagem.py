custo = float(input('Digite quantos km serão rodados na viagem: '))
passagem = float(0.50)
longa = float(0.45)
longa2 = int(200)

if custo <= longa2:
    print('A viagem vai sair no valor de R${} '.format(custo * passagem))
else:
    print('A viagem vai sair no valor de R${}'.format(custo * longa))


