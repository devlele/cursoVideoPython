import math

angulo = float(input('Informe um angulo qualquer: '))

print('O seno desse angulo é {:.3f}, o cosseno é {:.3f} e a tangente é {:.3f}'.format(math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo)))) #os parametros dessas finções estão em radianos, por isso não funciona da forma correta. precisa usar a função radians para converter em radianos