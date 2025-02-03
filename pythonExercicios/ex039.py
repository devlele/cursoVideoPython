from datetime import date

ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
tempo = int 

if idade < 18:
    tempo = 18 - idade
    print('Ainda não é hora de se alistar.\nFaltam {} anos'.format(tempo))

elif idade > 18:
    tempo = idade - 18
    print('você deveria ter se alistado {} anos atrás'.format(tempo))

else:
    print('Esse ano você completa 18 anos.\nEstá na hora de se alistar!')