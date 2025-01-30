ladoA = float(input('Digite a primeira reta: '))
ladoB = float(input('Digite a segunda reta: '))
ladoC = float(input('Digite a terceira reta: '))

if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    print('Pode ser formado um triangulo')
else:
    print('Não pode ser formado um triangulo')