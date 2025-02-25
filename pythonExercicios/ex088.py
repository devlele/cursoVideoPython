import random
import time

listaPrinc = []
listaRadom = 0

jogos = int(input('Quantos jogos deseja gerar? '))
for i in range(0, jogos):
    listaRadom = random.sample(range(1, 60), 6)
    listaPrinc.append(listaRadom)
    listaRadom = 0
cont = 1
for i in listaPrinc:
    print(f'Jogo {cont}: {i}')
    cont += 1
    time.sleep(0.75)