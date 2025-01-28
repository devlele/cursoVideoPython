dias = int(input('Quantos dias o carro foi alugado? '))
kms = float(input('Quantos Km foram rodados?'))
custo = dias*60 + kms*0.15

print('O total a pagar é de {} reais'.format(custo))
