lista = []
cont = 0
continua = ''
num = 0

while continua != 'n':
    num = int(input('Digite um valor: '))
    lista.append(num)
    cont += 1
    continua = input('Deseja continuar? [s/n]: ').strip().lower()

lista.sort(reverse = True)
print(f'Foram digitados {cont} números\n{lista}')
if 5 in lista:
    print('O número 5 foi digitado e está na lista')
else:
    print('O número 5 não foi digitado e não está na lista')
