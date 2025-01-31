numero = int(input('Digite um número inteiro: '))
base = int(input('Qual será a base de conversão?\nDigite "1" para converter em binário\nDigite "2" para converter em octal\nDigite "3" para converter em hexadecimal'))
resultado = 0

if base == 1:
    resultado = bin(numero)
elif base == 2:
    resultado = oct(numero)
else:
    resultado = hex(numero)

print('O número convertido é {}'.format(resultado[2:]))