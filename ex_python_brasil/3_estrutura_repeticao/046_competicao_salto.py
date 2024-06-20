'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. 
Os saltos são informados na ordem da execução, portanto não são ordenados. 
O programa deve ser encerrado quando não for informado o nome do atleta. 
A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
'''

# Número de saltos que cada atleta deve realizar
SALTOS = 5

# Lista com os nomes dos saltos para facilitar a impressão organizada
ordens_saltos = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

# Loop principal que continua solicita novos atletas
while True:
    nome_atleta = input('Informe o seu nome: ')

    distancias_saltos = [] # Lista para armazenar as distâncias dos saltos

     # Interrompe o loop no caso de nome menor que 1 ou se não for informado o nome do atleta
    if len(nome_atleta) <= 1:
        break  

    # Loop para obter as distâncias dos saltos    
    for i in range(SALTOS):
        distancia = float(input(f'Informe a distância do {ordens_saltos[i]} Salto: '))
        distancias_saltos.append(distancia)
   
   # Exibe cada salto e sua respectiva distância e o nome do atleta
    print(f'\nAtleta: {nome_atleta}\n')

    for ordem, salto in zip(ordens_saltos, distancias_saltos):
        print(f'{ordem} Salto: {salto} m')
         
    # Armazena o melhor e o pior salto     
    melhor_salto = max(distancias_saltos)
    pior_salto = min(distancias_saltos)

    # Encontra índices do melhor e pior salto
    index_melhor = distancias_saltos.index(melhor_salto)
    index_pior = distancias_saltos.index(pior_salto)

    # Remove o melhor e o pior salto, começando pelo de maior índice para não deslocar o outro
    if index_melhor > index_pior:
        distancias_saltos.pop(index_melhor)
        distancias_saltos.pop(index_pior)
    else:
        distancias_saltos.pop(index_pior)
        distancias_saltos.pop(index_melhor)

    # Calcula a média dos três saltos restantes
    media = sum(distancias_saltos) / 3

    # Exibe o restante do resultado
    print(f'\nMelhor salto: {melhor_salto} m')
    print(f'Pior salto: {pior_salto} m')
    print(f'Média dos demais saltos: {media:.2f} m\n')
    
    print('Resultado final:')
    print(f'{nome_atleta}: {media:.2f} m\n')
    