ladoA = float(input('Digite a primeira reta: '))
ladoB = float(input('Digite a segunda reta: '))
ladoC = float(input('Digite a terceira reta: '))

if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    if ladoA ==  ladoB and ladoA == ladoC:
        print('Pode ser formado um triangulo equilatero (com todos os lados iguais)!')
    elif ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
        print('Pode ser formado um triangulo escaleno (com todos os lados diferentes)!')
    else:
        print('Pode ser formado um triangulo isósceles (com dois lados iguais)!')
else:
    print('Não pode ser formado um triangulo')
