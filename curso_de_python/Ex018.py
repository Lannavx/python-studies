#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
n1 = float(input('Informe um ângulo: '))
rad = math.radians(n1)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f'O valor de seno é {seno:.2f} \nO valor do cosseno é {cosseno:.2f} \nO valor da tangente é {tangente:.2f}')