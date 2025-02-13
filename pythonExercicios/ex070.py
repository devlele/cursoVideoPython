class Produto:
    def __init__(self, nome='', preco=0.0):
        self.nome = nome
        self.preco = preco
    
    def receberDados(self):
        self.nome = input('Informe o nome do produto: ')
        self.preco = float(input('Informe o preço do produto: '))
    
def CalcGasto():
    valor = 0.0
    for produto in produtos:
        valor += produto.preco
    return valor

def maisMil():
    cont = 0
    for produto in produtos:
        if produto.preco > 1000:
            cont += 1

    return cont

def maisBarato():
    prodBarato = ''
    comp = float('inf')
    for produto in produtos:
        if produto.preco < comp:
            prodBarato = produto.nome
    
    return prodBarato

produtos = []
while True:
    produto = Produto()
    produto.receberDados()
    produtos.append(produto)

    continuar = input('Deseja continuar? [S/N]: ').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Deseja continuar? [S/N]: ').upper()
    if continuar == 'S':
        continue
    else: 
        break


totalGasto = CalcGasto()
contMaisMil = maisMil()
barato = maisBarato()

print(f'''O gasto total foi de: {totalGasto}
{contMaisMil} produtos custam mais de R$1000,00
O produto mais barato é: {barato}''')