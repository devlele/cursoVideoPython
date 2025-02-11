num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
indice = 0

while indice != 5:
    indice = int(input('O que deseja fazer?\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n'))
    if indice == 1:
        soma = num1 + num2
        print('A soma é {}'.format(soma))
        continue
    
    elif indice == 2:
        multi = num1 * num2
        print('A multiplicação é {}'.format(multi))
        continue
    
    elif indice == 3:
        if num1 > num2:
            print('{} É maior que {}'.format(num1, num2))
            continue
        elif num2 > num1:
            print('{} É maior que {}'.format(num2, num1))
            continue
        else:
            print('Os números são iguais')
            continue
    
    elif indice == 4:
        num1 = float(input('Digite o novo valor: '))
        num2 = float(input('Digite o novo valor: '))
        continue