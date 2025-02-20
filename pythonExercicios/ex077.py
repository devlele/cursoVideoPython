palavras = ('aprender', 'ensinar', 'estudar', 'avaliar', 'azul', 'ausencia', 'cigarro', 'queijo', 'barato', 'bagulho')
#vogais = ''
#palavra = []

#for i in palavras:
#    palavra = i
#    for i in palavra:
#        
#        if i == 'a':
#            vogais += ' ' + i
#        if i == 'e':
#            vogais += ' ' + i
#        if i == 'i':
#            vogais += ' ' + i
#        if i == 'o':
#            vogais += ' ' + i
#        if i == 'u':
#            vogais += ' ' + i

#    print(f'Na palavra {palavra.upper()} temos {vogais}')
#    vogais = '' 

# A parte comentada foi a minha primeira solução, a não comentada é a solução melhorada 
for i in palavras:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for letra in i:
        if letra in 'aeiou':
            print(letra, end=' ')
    
    