'''Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.'''

def imprimir_sequencia(n):
    '''Imprime uma sequência crescente de números para cada linha, começando em 1 e 
    aumentando até o valor de n'''
    for i in range(1, n + 1): 
        for num in range(1, i + 1):
             print(num, end=' ') 
        print()

# Solicita ao usuário um número
n = int(input('Informe um número: '))

# Chama a função com o número informado pelo usuário
imprimir_sequencia(n)   