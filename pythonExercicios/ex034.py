salario = float(input('Informe o salario do funcionário: '))

if salario > 1250:
    print('O salario terá um aumento de {:.2f} reais'.format(salario*0.10))
else:
    print('O salario terá um aumento de {:.2f} reais'.format(salario*0.15))