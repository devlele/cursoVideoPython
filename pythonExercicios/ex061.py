num = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Informe a razão: '))
termo = num
cont = 1

while cont <= 10:
    print(termo)
    termo += razao
    cont += 1