valores = []
continua = ''

while continua != 'N':
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
    else:
        print('Valor duplicado! Não será adicionado.')

    continua = input('Deseja continuar? [S/N]: ').strip().upper()
    
    
valores.sort()
print(valores)