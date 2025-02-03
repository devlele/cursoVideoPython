valor = float(input('Digite o valor da compra: '))
pagamento = int(input('Escolha a forma de pagamento \n1 para dinheiro ou cheque \n2 para cartão \n'))
valorFinal = float


if pagamento == 2:
    formaPagamento = input('Deseja parcelar? (s/n): ')

    if formaPagamento == 's':
        parcelas = int(input('Em quantas vezes deseja parcelar?: '))

        if parcelas > 2:
            valorFinal = valor * 1.20

        else:
            valorFinal = valor

    else:
        valorFinal = valor * 0.95

else:
    valorFinal = valor * 0.90

print('Valor a ser pago: {:.2f} \nObrigado pela compra!'.format(valorFinal))



