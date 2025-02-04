frase = input('Digite uma frase: ').strip().lower().replace(' ', '')
fraseInvertida = ''

for i in reversed(frase):
    fraseInvertida += i

if frase == fraseInvertida:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

