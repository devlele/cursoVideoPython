class Pessoa: #criação de uma classe ara armazernar todos os dados necessários
    def __init__(self, nome='', idade=0, sexo=''):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def receberDados(self):
        self.nome = input('Informe o nome: ')
        self.idade = int(input('Informe a idade: '))
        self.sexo = input('Informe o sexo [m/f]: ')

    def exibir(self):
        print('Nome: {}\nIdade: {}\nSexo: {}'.format(self.nome, self.idade, self.sexo))

def calcMedia():#Função que calcula a média das idades cadastradas
    soma = 0
    for pessoa in pessoas:
        soma += pessoa.idade
    media = soma / len(pessoas)
    return media

def homemVelho():#Função para achar o nome do homem mais velho
    maisVelho = 0
    nomeVelho = ''
    for pessoa in pessoas:
        if pessoa.sexo == 'm':
            if pessoa.idade > maisVelho:
                maisVelho = pessoa.idade
                nomeVelho = pessoa.nome

    return nomeVelho

def calcMulherMenosVinte():#função para calcular a quantidade de mulheres com menos de 20 anos
    cont = 0
    for pessoa in pessoas:
        if pessoa.sexo == 'f':
            if pessoa.idade < 20:
                cont += 1
    
    return cont

pessoas = []#lista para armazenar os dados recebdos dentro do for

for i in range(0, 4):
    print('Cadastro da {}ª pessoa'.format(i+1))
    pessoa = Pessoa()#Criação de um objeto pessoa
    pessoa.receberDados()
    pessoas.append(pessoa)#append é um método de adicionar elementos em uma lista

mediaIdades = calcMedia()
homemMaisVelho = homemVelho()
mulherMenosVinte = calcMulherMenosVinte()

print('Média de idades: {}\nHomem mais velho: {}\nQuantidade de mulheres abaixo dos 20 anos: {}'.format(mediaIdades, homemMaisVelho, mulherMenosVinte))

