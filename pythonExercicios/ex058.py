from random import randint
from time import sleep #o metodo sleep faz o computador demorar alguns minutos para executar um comando

numSecret = randint(0, 10)
num = int(input('Tente adivinhar o número secreto\nDigite um número de 0 a 10: '))
cont = 1

while num != numSecret:
    num = int(input('Errou. Mas tente novamente!\nDigite um número novamente: '))
    cont += 1

print('Parabéns!!\nVocê adivinhou o número secreto em {} tentativas!'.format(cont))