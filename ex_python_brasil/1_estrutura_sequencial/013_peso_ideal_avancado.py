"""
    Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
        1.Para homens: (72.7*h) - 58
        2.Para mulheres: (62.1*h) - 44.7
"""

genero = input('Informe se você é homem ou mulher: ').lower()
altura = float(input('Informe sua altura: '))
formula_mulheres = (62.1 * altura) - 44.7
formula_homens = (72.7 * altura) - 58

if genero == 'mulher':
    print(f'Seu peso ideal é {formula_mulheres:.2f}')
elif genero == 'homem':
    print(f'Seu peso ideal é {formula_homens:.2f}')
else:
    print('Genêro não identificado')