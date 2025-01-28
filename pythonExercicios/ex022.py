nome = input('Insira seu nome completo: ').strip()

print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(" ",""))))
espaco = nome.find(" ")
print('Seu primeiro nome é {} e tem {} letras'.format(nome[:espaco], len(nome[:espaco])))

