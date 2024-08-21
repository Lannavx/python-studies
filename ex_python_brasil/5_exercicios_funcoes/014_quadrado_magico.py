'''Quadrado mágico. 
Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição 
e no qual a soma das linhas, colunas e diagonais é a mesma. 
Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4 
1  5  9
6  7  2

Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.'''


import itertools

def verificar_quadrado_magico(matriz):
    '''Verifica se a soma das linhas, colunas e diagonais é a mesma'''

    soma_esperada = 15
    
    # Verifica as linhas
    for i in range(3):
        soma_linha = 0
        for j in range(3):
            soma_linha += matriz[i][j]
        if soma_linha != soma_esperada:
            return False
    
    # Verifica as colunas
    for i in range(3):
        soma_coluna = 0
        for j in range(3):
            soma_coluna += matriz[j][i]
        if soma_coluna != soma_esperada:
            return False
    
    # Verifica as diagonais
    soma_diagonal_1 = 0
    for i in range(3):
        soma_diagonal_1 += matriz[i][i]
    if soma_diagonal_1 != soma_esperada:
        return False
    
    soma_diagonal_2 = 0
    for i in range(3):
        soma_diagonal_2 += matriz[i][2-i]
    if soma_diagonal_2 != soma_esperada:
        return False
    
    return True

def fazer_quadrados_magicos():
    '''Exibe todas as combinações possíveis do quadrado mágico '''

    # Gera todas as permutações possíveis da lista
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    permutacoes = itertools.permutations(numeros)
    
    quadrados_magicos = []
    
    # Organiza a permutação em uma matriz de 3x3
    for p in permutacoes:
        matriz = []
        matriz.append([p[0], p[1], p[2]])
        matriz.append([p[3], p[4], p[5]])
        matriz.append([p[6], p[7], p[8]])
        
        # Verifica se é um quadrado mágico
        if verificar_quadrado_magico(matriz):
            quadrados_magicos.append(matriz)
    
    # Mostra todos os quadrados mágicos encontrados
    for matriz in quadrados_magicos:
        for linha in matriz:
            print(linha)
        print()  

fazer_quadrados_magicos()
