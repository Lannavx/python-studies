'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random
numero = int(input('Informe um número entre 0 e 5: '))
lista = [1,2,3,4,5]
n1 = random.choice(lista)
if numero == n1:
   print('Você acertou!')
else:
    print('Você errou!')

#Outra forma de fazer

from random import randint
jogador = int(input('Informe um número entre 0 e 5: '))
computador = randint(0,5)
if jogador == computador:
   print('Você acertou!')
else:
    print(f'Você errou! Eu pensei no número {computador}')