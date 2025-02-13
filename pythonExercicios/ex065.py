media = 0.0
maior = 0
menor = float('inf')
continua = 's'
num = 0
cont = 0
soma = 0

while continua == 's':
    num = int(input('Digite um número inteiro: '))
    soma += num

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    cont += 1
    continua = input('Deseja continuar? [s/n]: ').lower()

media = soma / cont

print('A média entre os números é: {}\nO maior foi: {}\nO mmenor foi: {}'.format(media, maior, menor))