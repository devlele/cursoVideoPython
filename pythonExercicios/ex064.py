cont = 0
soma = 0
num = int(input('Digite um número: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))

print('Foram digitados {} numeros e a soma deles é {}'.format(cont, soma))