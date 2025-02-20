lista = []
listaPar = []
listaImpar = []
num = 1

print('Para sair do loop digite um número negativo!')
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    lista.append(num)

    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

print(f'''Lista completa:
{lista}
Lista par
{listaPar}
lista impar
{listaImpar}''')