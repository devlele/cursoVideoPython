km = float(input('O carro está a quantos km/h? '))

if km > 80:
    multa = (km-80) * 7
    print('Você recebeu uma multa de {:.2f} reais'.format(multa))

