''' Numa eleição existem três candidatos. 
Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''

# Solicita ao usuário a entrada do número total de eleitores
eleitores = int(input('Informe o número total de eleitores: '))

# Inicializa um dicionário para armazenar os candidatos e suas contagens de votos
candidatos = {'1': ['Candidato 1', 0], '2': ['Candidato 2', 0], '3': ['Candidato 3', 0]}

# Imprime instruções e abre a votação
print('-' * 10)
print('Votação aberta!')
print('Caro eleitor, dê o seu voto para o candidato escolhido!')
print('''
1 - Candidato 1
2 - Candidato 2
3 - Candidato 3
''')

# Loop para processar os votos de todos os eleitores
for i in range(eleitores):
    voto = input(f'Eleitor {i+1}, informe seu voto: ')

    # Verifica se o voto é válido 
    while voto not in candidatos:
        print('Voto desconsiderado! Por favor, vote no número correto de seu candidato.') 
        voto = input(f'Eleitor {i+1}, informe seu voto: ')      
    
    # Incrementa a contagem de votos para o candidato escolhido
    candidatos[voto][1] += 1

    print('Voto computado, obrigada!')

print('-' * 10)

# Imprime a contagem final de votos para cada candidato
print('Contagem de votos:')
for chave, valor in candidatos.items():
    print(f'{valor[0]} recebeu {valor[1]} votos!')


