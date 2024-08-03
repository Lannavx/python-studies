'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta 
em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
O programa deve ser encerrado quando não for informado o nome do atleta. 
A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''

SALTOS = 5

# Lista para facilitar a impressão organizada
ordens_saltos = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

# Loop principal que continua solicita novos atletas
while True:
    nome_atleta = input('Atleta: ').strip()

    # Interrompe o loop no caso de nome não informado
    if not nome_atleta:
        print('Programa encerrado. Nenhum nome fornecido.')
        break

    # Lista para armazenar as distâncias dos saltos
    distancias_saltos = [] 

    # Loop para obter as distâncias dos saltos    
    for i in range(SALTOS):
        distancia = float(input(f'{ordens_saltos[i]} Salto: '))
        distancias_saltos.append(distancia)

    media_salto = sum(distancias_saltos) / SALTOS

    print('\nResultado final:\n')
    print(f'Atleta: {nome_atleta}')
    print(f'Saltos: {' - '.join(map(str, distancias_saltos))}')
    print(f'Média dos saltos: {media_salto:.1f} m\n')
    