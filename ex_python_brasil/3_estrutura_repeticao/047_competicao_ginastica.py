'''Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta 
em sua apresentação e depois informe a sua média, conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
As notas não são informados ordenadas. 
Um exemplo de saída do programa deve ser conforme abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04'''

# Número de notas 
NOTAS = 7

# Loop principal que continua solicitando novas notas
while True:
    nome_ginasta = input('Informe o nome do atleta (ou pressione ENTER para sair): ')

    # Condição de parada do loop
    if nome_ginasta == '':
        break

    # Lista para armazenar as notas
    lista_notas = []

    # Loop para obter as notas para cada atleta
    for _ in range(NOTAS):
        notas_jurados = float(input(f'Jurado, por favor, informe a nota para o atleta {nome_ginasta}: '))
        lista_notas.append(notas_jurados)
   
    # Exibe as notas e o nome do atleta
    print(f'\nAtleta: {nome_ginasta}')
    for nota in lista_notas:
        print(f'Nota: {nota}')
         
    # Armazena a melhor e a pior nota     
    melhor_nota = max(lista_notas)
    pior_nota = min(lista_notas)

    # Encontra índices da melhor e pior nota
    index_melhor = lista_notas.index(melhor_nota)
    index_pior = lista_notas.index(pior_nota)

    # Remove a melhor e o pior nota, começando pelo de maior índice para não deslocar o outro
    if index_melhor > index_pior:
        lista_notas.pop(index_melhor)
        lista_notas.pop(index_pior)
    else:
        lista_notas.pop(index_pior)
        lista_notas.pop(index_melhor)

    # Calcula a média das notas restantes
    media = sum(lista_notas) / (NOTAS - 2)

    # Exibe o restante do resultado
    print('\nResultado final:')
    print(f'Atleta: {nome_ginasta}')
    print(f'Melhor nota: {melhor_nota}')
    print(f'Pior nota: {pior_nota}')
    print(f'Média: {media:.2f}\n')
    