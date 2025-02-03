peso = float(input('Informe seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso/altura**2

if imc < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso'.format(imc))
elif imc < 25:
    print('Seu IMC é {:.2f} e você está com um peso ideal'.format(imc))
elif imc < 30: 
    print('Seu IMC é {:.2f} e você está com sobrepeso'.format(imc))
elif imc < 40:
    print('Seu IMC é {:.2f} e você esta com obesidade'.format(imc))
else:
    print('Seu IMC é {:.2f} e você está com obesidade mórbida'.format(imc))