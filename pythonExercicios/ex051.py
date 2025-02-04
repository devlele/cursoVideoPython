num = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Informe a razão: '))

for i in range(num, num+10*razao, razao):
    print(i)