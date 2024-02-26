from math import sin, cos, tan, radians

ang = float(input('Digite o ângulo: '))
sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print('O valor do ângulo {:.2f} em seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(ang, sen, coss, tang))