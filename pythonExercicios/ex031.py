distancia = float(input('Qual a distância da viagem em kms? '))

if distancia > 200:
    print('O valor da passagem será {:.2f} reais'.format(distancia*0.45))
else:
    print('O valor da passagem será {:.2f} reais'.format(distancia*0.50))