'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.'''

#Maneira 1
from math import sqrt
cateto1 = float(input('Insira um número: '))
cateto2 = float(input('Insira outro número: '))
formula = (pow(cateto1,2) + pow(cateto2,2))
print(f'O comprimento da hipotenusa considerando o cateto aposto como {cateto1} e o cateto adjacente como {cateto2} é de {sqrt(formula):.2f}')

#Maneira 2

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hi = math.hypot(co,ca)
print(f'A hipotenusa vai medir {hi:.2f}')