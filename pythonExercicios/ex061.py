num = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Informe a razão: '))

cont = num
while cont < num + 10 * razao:
    print(cont)
    cont += razao 