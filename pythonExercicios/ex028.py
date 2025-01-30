from random import randint
from time import sleep #o metodo sleep faz o computador demorar alguns minutos para executar um comando

numSecret = randint(0, 5)
num = int(input('Tente adivinhar o número secreto\nDigite um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(2) #dentro do parenteses informa o tempo em segundos que ele vai esperar para executar
if numSecret == num:
    print('Parabéns!!\nVocê adivinhou o número secreto!')
else:
    print('Poxa, não foi dessa vez :(')