'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

#Forma 1

# No sample, especificamos um intervalo e fornecemos quantos números aleatórios precisamos gerar

from random import sample

num_sortido = (sample(range(1,11),5))
print(f'Os valores sorteados foram: {num_sortido}')

print(f'O maior valor sorteado foi {max(num_sortido)}')
print(f'O menor valor sorteado foi {min(num_sortido)}')

#Forma 2

from random import randint

num = (randint(1,11), randint(1,11), randint(1,11), randint(1,11), randint(1,11))
print(f'Os valores sorteados foram: ', end = '')
for n in num:
    print(f'{n} ', end = '')
    
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')