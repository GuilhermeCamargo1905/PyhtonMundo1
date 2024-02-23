print('O limite de velocidade é 80km/h')
limite = float(80)
velocidade = float(input('Qual a velocidade do carro: '))
multa = float((velocidade - limite) * 7.00)

if velocidade <= limite:
    print('Você não foi multado! sua velocidade era {}km/h e o limite é {}km/h'.format(velocidade,limite))
else:
    print('Você foi multado o limite era {}km/h você estava a {}km/h sua multa é no valor de {}'.format(limite, velocidade, multa))
