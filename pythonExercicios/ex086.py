matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor do elemento [{i, j}]: '))

for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]:^5}', end=' ')
    print()
    