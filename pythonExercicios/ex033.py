num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
num3 = float(input('Digite o 3º número: '))

if num1 > num2 and num1> num3:
    if num2 > num3:
        print('O maior número é {} e o menor é {}'.format(num1, num3))
    else:
        print('O maior número é {} e o menor é {}'.format(num1, num2))
if num2 > num1 and num2 > num3:
    if num1 > num3:
        print('O maior número é {} e o menor é {}'.format(num2, num3))
    else:
        print('O maior número é {} e o menor é {}'.format(num2, num1))
if num3 > num2 and num3> num1:
    if num2 > num1:
        print('O maior número é {} e o menor é {}'.format(num3, num1))
    else:
        print('O maior número é {} e o menor é {}'.format(num3, num2))