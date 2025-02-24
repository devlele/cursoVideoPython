listaNumeros = [[], []]


for i in range(0, 7):
    num = int(input(f'Digite o {i+1}º valor: '))
    if num % 2 == 0:
        listaNumeros[1].append(num)
    else:
        listaNumeros[0].append(num)

listaNumeros[0].sort()
listaNumeros[1].sort()
print(f'''Os valores pares digitados foram: {listaNumeros[1]}
Os valores impares digitados foram: {listaNumeros[0]}''')