valores = tuple(int(input('Digite o valor desejado: ')) for _ in range(4)) #o '_' é utilizado por ser uma variavel descartavel, ou seja não será usada dentro do loop
cont9 = 0
valor3 = f'O valor 3 apareceu na {valores.index(3) + 1}ª posição'
pares = []
for i in valores:
    if i == 9:
        cont9 +=1

    if i % 2 == 0:
        pares.append(i)
    
    if valores.index(3) == False:
        valor3 = 'O valor três não foi digitado em nenhuma posição'

print(f'''O valor 9 apareceu {cont9} vezez
{valor3}
Os valores pares digitados foram {pares}''')