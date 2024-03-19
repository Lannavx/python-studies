#Faça um programa que leia um número qualquer e mostre o seu fatorial.

#Forma 1 
from math import factorial
num = int(input('Informe um número para calcular seu Fatorial: '))
fatorial = factorial(num)
print(f'O fatorial de {num} é {fatorial}')

#Forma 2 com while
num = int(input('Informe um número: '))
cont = num
fatorial = 1
print(f'Calculando {num}! = ', end='')
while cont > 0 :
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print(f'{fatorial}')

#Forma 3 com for
numero = int(input("Digite um número para calcular o seu fatorial: "))
fatorial = 1
for c in range(1, numero + 1):
    fatorial *= c 
print(f"O fatorial de {numero} é {fatorial}")