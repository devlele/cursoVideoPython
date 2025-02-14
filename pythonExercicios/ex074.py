from random import randint

numeros = tuple(randint(1, 100) for _ in range(5))
print(numeros)
print(f'''O menor valor é {min(numeros)}
E o maior é {max(numeros)}''')
