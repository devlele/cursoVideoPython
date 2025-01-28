import math

oposto = float(input('Informe o comprimento do cateto oposto: '))
adjacente = float(input('Informe o comprimento do cateto adjacente: '))

hipo = math.hypot(oposto, adjacente)

print('A hipotenesa do triangulo é {:.2f}'.format(hipo))