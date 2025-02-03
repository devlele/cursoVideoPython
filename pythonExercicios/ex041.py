from datetime import date

ano = int(input('Informe o ano em que você nasceu: '))
idade = date.today().year - ano
categoria = str

if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Junior'
elif idade <= 20:
    categoria = 'Sênior'
else:
    categoria = 'Master'

print(categoria)