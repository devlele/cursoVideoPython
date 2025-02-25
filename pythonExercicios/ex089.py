listaGeral = []
listaAluno = []
listaMedias = []
media = 0.0
continua = ''

while True:
    listaAluno.append(input('Nome: '))
    listaAluno.append(float(input('Nota 1: ')))
    listaAluno.append(float(input('Nota 2: ')))
    listaGeral.append(listaAluno[:])
    listaAluno.clear()
    continua = input('Deseja continuar? [s/n]: ')
    if continua in 'Nn':
        break

for i in range(0, len(listaGeral)):
    media = (listaGeral[i][1] + listaGeral[i][2])/2
    listaMedias.append(media)

print('-='*50)
for i in range(0, len(listaGeral)):
    print(i, end=' ')
    print(listaGeral[i][0], end=' ')
    print(listaMedias[i], end=' ')
    print()


num = 0
while num != 999:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num > (len(listaGeral) - 1):
        print('Aluno não existe')
        continue
    print(f'As notas de {listaGeral[num][0]} são {listaGeral[num][1:]}' )
    



























