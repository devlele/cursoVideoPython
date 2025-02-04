from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Suas opções: \n0 PEDRA\n1 PAPEL\n2 TESOURA')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

print('-='*12)
print('O computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-='*12)

if computador == jogador:
    print('O jogo empatou!')

elif computador == 0:
    if jogador == 1:
        print('Você ganhou!')
    else:
        print('Você perdeu!')

elif computador == 1:
    if jogador == 0:
        print('Você perdeu!')
    else:
        print('Você ganhou!')

else:
    if jogador == 0:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
