num = int(input('Informe um número: '))
uni = num % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num //1000 

print('Analisando o número...')
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\n'.format(uni, dez, cen, mil))
