'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Fortaleza.''' 
           
#Lembrando que a contagem começa em ZERO           
times = ('Palmeiras', 'Grêmio', 'Atlético', 'Flamengo', 'Botafogo', 
         'Red Bull Bragantino', 'Fluminense', 'Athletico', 'Internacional', 
         'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco',
         'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América')

print('-=' * 20)
print(f'Lista de Times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 5 primeiros times são {times[:5]}')
print('-=' * 20)
print(f'Os últimos 4 colocados são {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print(f'O Fortaleza está na {times.index('Fortaleza')+1}ª posição.')