from random import randint

num = int(input('Digite um número: '))
numCompu = randint(0, 10)
soma = num + numCompu
parImpar = input('Você quer par ou ímpar? [p/i]').strip().lower()
cont = 0

while True:
    if parImpar == 'p':
        if soma % 2 == 0:
            print('Você ganhou!\nVamos jogar de novo...')
            cont +=1
        else:
            print('Você perdeu!')
            break

    else:
        if soma % 2 == 0:
            print('Você perdeu!')
            break
        else:
            print('Você ganhou!\nVamos jogar de novo...')
            cont +=1

    num = int(input('Digite um número: '))
    parImpar = input('Você quer par ou ímpar? [p/i]').strip().lower()

print(f'Você ganhou {cont} vezes')