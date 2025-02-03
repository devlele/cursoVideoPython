valorCasa = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual a sua renda? '))
anos = int(input('Em quantos anos deseja pagar? '))
valorPrest = valorCasa/anos/12

print('Para pagar uma casa de {:.2f} reais em {} anos a prestação será de {:.2f} reais'.format(valorCasa, anos, valorPrest))

if valorPrest > salario * 0.3:
    print('Infelizmente o seu financiamento foi negado')

else:
    print('Financiamento aprovado!')