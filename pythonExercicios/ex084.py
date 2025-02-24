temp = []
princ = []
listMaior = []
listMenor = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = input('Quer continuar? [s/n]: ')
    if resp in 'nN':
        break

for i in princ:
    if i[1] == maior:
        listMaior.append(i[0])
    if i[1] == menor:
        listMenor.append(i[0])

print(f'''Tivemos ao todo {len(princ)} cadastros
O maior peso é {maior}Kg e {listMaior} possuem este peso
O menor peso é {menor} e {listMenor} possuem este peso''')