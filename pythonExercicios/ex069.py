idade = 0
sexo = ''
continuar = ''
cont18 = 0
contHomens = 0
contMulheres = 0
print('='*20, 'Cadastro de pessoas', '='*20 )

while True:
    idade = int(input('Informe a sua idade: '))
    sexo = input('Informe o seu sexo [M/F]: ').upper()
    print('='*25)

    while sexo != 'M' and sexo != 'F':
        sexo = input('Informe o seu sexo [M/F]: ').upper()
    
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        contHomens += 1
    else:
        if idade < 20:
            contMulheres += 1
    
    continuar = input('Deseja continuar? [S/N]: ').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar? [S/N]: ').upper()

    if continuar == 'S':
        continue
    else:
        break

print(f'''Total de pessoas com mais de 18 anos: {cont18}
Total de homens cadastrados: {contHomens}
Total de mulheres com menos de 20 anos: {contMulheres}''')
    
