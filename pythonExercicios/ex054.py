from datetime import date

ano = 0
somaMaior = 0
somaMenor = 0

for i in range(0,7):
    ano = int(input('Infrome o ano de nascimento da {}ª pessoa: '.format(i+1)))

    if date.today().year - ano < 18:
        somaMenor += 1
    else:
        somaMaior += 1

print('{} pessoas ainda são menores\n{} pessoas já são maiores'.format(somaMenor, somaMaior)) 