nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('Média {}.\nAluno reprovado!'.format(media))

elif media > 5 and media < 7:
    print('Média {}.\nAluno em recuperação!'.format(media))

else:
    print('Média {}.\nAluno aprovado!'.format(media))