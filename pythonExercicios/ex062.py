num = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Informe a razão: '))
termo = num
cont = 1
total = 0
vezes = 10

while vezes != 0:
    total = total + vezes
    while cont <= total:
        print(termo)
        termo += razao
        cont += 1
    vezes = int(input('eseja mostrar mais quantos termos?'))