import random

nomes_alunos = []

for i in range(4):
    nome = input(f'Digite o {i+1}º nome: ')
    nomes_alunos.append(nome)

random.shuffle(nomes_alunos)

print('A ordem de apresentação será:\n', nomes_alunos)
