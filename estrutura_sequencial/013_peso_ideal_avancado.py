"""
    Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
        1.Para homens: (72.7*h) - 58
        2.Para mulheres: (62.1*h) - 44.7
"""

genero = input(' ')
altura = float(input('Informe sua altura: '))

para_mulheres = (62.1*altura) - 44.7
para_homens = (72.7*altura) - 58

