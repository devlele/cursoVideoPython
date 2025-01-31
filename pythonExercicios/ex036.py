valorCasa = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual a sua renda? '))
anos = int(input('Em quantos anos deseja pagar? '))
valorPrest = valorCasa/anos/12

if valorPrest > salario * 0.3:
    print('Infelizmente o seu financiamento foi negado')

else:
    print('Financiamento aprovado!\nVocê pode parcelar seu imóvel em {} parcelas de {:.2f} reais'.format(anos * 12, valorPrest))