num = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Informe a razão: '))
vezes = 0
cont = num
while cont < num + (10 + vezes) * razao:
    print(cont)
    cont += razao 
    
    if cont == num + (10 + vezes) * razao:
        vezes = int(input('Deseja mostrar mais quantos termos? '))
        if vezes != 0:
            continue
        else:
            break