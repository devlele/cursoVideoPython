times = ('Atletico mineiro', 'Bahia', 'Botafogo', 'Ceara', 'Corinthias', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventos', 'Mirasol', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo', 'Sport', 'Vasco', 'Vitória')

print(f'''Os 5 primeiros colocados são: {times[:5]}
Os quatro últimos são? {times[16:]}
Times em ordem alfabética:
{sorted(times)}
O São Paulo está na posição: {times.index('São Paulo')}''')