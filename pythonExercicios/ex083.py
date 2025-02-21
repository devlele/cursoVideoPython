expressao = input('Digite uma expressão númerica: ')
pilha = []

for i in expressao:
    if i == "(":
        pilha.append(i)
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
    
if len(pilha) == 0:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')

#abre = 0
#fecha = 0
#for i in expressao:
#    if i == '(':
#        abre += 1
#    if i == ')':
#        fecha += 1
    
#if abre == fecha:
#    print('A expressão é válida!')
#else:
#    print('A expressão é inválida!')
