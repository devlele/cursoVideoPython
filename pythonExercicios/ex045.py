from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Suas opções: \n0 PEDRA\n1 PAPEL\n2 TESOURA')
jogador = int(input('Qual é a sua jogada? '))

print('O computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))

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
