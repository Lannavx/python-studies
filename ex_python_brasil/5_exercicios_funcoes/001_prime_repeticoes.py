'''Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.'''


def imprimir_valor(n):
    '''Imprime o número i, repetido i vezes, separado por espaço'''
    for i in range(1, n + 1):
        print((str(i) + ' ') * i)

# Solicita ao usuário um número
n = int(input('Informe um número: '))

# Chama a função com o número informado pelo usuário
imprimir_valor(n)   