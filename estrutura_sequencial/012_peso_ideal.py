"""
    Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal.
    Fórmula: (72.7*altura) - 58
"""

altura = float(input('Informe a sua altura: '))

peso_ideal = (72.7*altura) - 58

print(f'O seu peso ideal baseado na sua altura é {peso_ideal:.2f}')