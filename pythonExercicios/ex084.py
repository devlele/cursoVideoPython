cadastro = []
pesado = []
leve = []
cont = 0
continua = ''

while True:
    cadastro.append(input('Digite seu nome: '))
    cadastro.append(float(input('Digite seu peso: ')))
    cont += 1
    continua = input('Deseja continuar? [s/n]: ').lower()
    if continua == 'n':
        break

print(cadastro)