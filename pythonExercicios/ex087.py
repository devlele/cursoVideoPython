somaPares = 0
somaTercColuna = 0
maiorSegLinha = 0

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor do elemento [{i, j}]: '))
        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]

somaTercColuna = matriz[0][2] + matriz[1][2] + matriz[2][2]
maiorSegLinha = max(matriz[1])

for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]:^5}', end=' ')
    print()
    
print(f'''A soma de todos os valores pares é {somaPares}
A soma dos valores da terceira coluna é {somaTercColuna}
O maior valor da segunda linha é {maiorSegLinha}''')