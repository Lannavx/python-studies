"""
    Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
    Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
    que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        1. comprar apenas latas de 18 litros;
        2. comprar apenas galões de 3,6 litros;
        3. misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde 
        os valores para cima, isto é, considere latas cheias.
"""

import math
tamanho_area = float(input('Informe o tamanho da área a ser pintada em metros quadrados: '))
litragem = tamanho_area / 6

#latas
latas = math.ceil(litragem / 18)
preço_latas = latas * 80

#galões
galoes = math.ceil(litragem / 3.6)
preço_galoes = galoes * 25

#latas e galões com folga
litragem_folga = (litragem * 1.10)
if litragem_folga < 18:
    galoes_folga = math.ceil(litragem_folga / 3.6)
    latas_folga = 0
else:
    latas_folga = math.floor(litragem_folga / 18)
    resto_litragem = litragem_folga - (latas_folga * 18)
    galoes_folga = math.ceil(resto_litragem / 3.6)
    
preço_total = (latas_folga * 80) + (galoes_folga * 25)

print(f'\nA quantidade de litros de tinta necessários para pintar {tamanho_area}m são de: {litragem:.2f}L.')

print(f'''\nOpção 1: Apenas Latas
Serão necessárias {latas} latas de 18 litros com o custo total de R${preço_latas}''')
print(f'''\nOpção 2: Apenas Galões
Serão necessários {galoes} galões de 3,6 litros com o custo total de R${preço_galoes}''')
print(f'''\nOpção 3: Latas e Galões:
Serão necessárias {latas_folga} latas e {galoes_folga} galões com o custo total de R${preço_total:.2f}''')
    


