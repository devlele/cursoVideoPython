from bisect import insort

lista = []
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    insort(lista, num)
    print(f'O valor foi adicionado na posição {lista.index(num)}')

print(lista)