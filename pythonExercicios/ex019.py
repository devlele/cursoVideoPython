import random

nomes_alunos = []

for i in range(4):
    nome = input(f'Digite o {i+1}º nome: ')
    nomes_alunos.append(nome)

nome_sort = random.choice(nomes_alunos)
print('O nome sorteado foi {}'.format(nome_sort))