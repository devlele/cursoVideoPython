val = []
for i in range(0, 5):
    val.append(int(input('Digite um valor: ')))

print(f'O maior valor é {max(val)} na posição {val.index(max(val)) + 1}\nO menor valor é {min(val)} na posição {val.index(min(val)) + 1}')