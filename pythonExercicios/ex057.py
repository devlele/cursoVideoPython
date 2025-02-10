sexo = str(input('Informe seu sexo: ').strip().upper())

while sexo not in ('M', 'F'):
    print('Valor inválido!\nO sexo deve ser M ou F')
    sexo = input('Informe o sexo novamente: ').strip().upper()

print('Sexo válido!')