maior = 0.0
menor = float('inf')

for i in range(0, 5):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(i+1)))

    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print('O maior peso é {:.2f} e o menor é {:.2f}'.format(maior, menor))
